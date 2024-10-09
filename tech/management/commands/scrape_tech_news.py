# tech/management/commands/scrape_tech_news.py

from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from urllib.robotparser import RobotFileParser
from selenium.common.exceptions import WebDriverException, TimeoutException

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'franklymade.settings')
django.setup()

from tech.models import News, NewsCategory
from django.utils.text import slugify


# import for dynamic download of image into s3bucket
import requests
from django.core.files.base import ContentFile 

# handle the data saving error
from django.db import IntegrityError


from . import image_downloader




class Command(BaseCommand):
    help = 'Scrapes tech news from TechCrunch'

    def handle(self, *args, **kwargs):
        self.scrape_tech_news()

    def is_scraping_allowed(self, base_url, user_agent="*"):
        robots_url = f"{base_url}/robots.txt"
        robot_parser = RobotFileParser()
        robot_parser.set_url(robots_url)
        robot_parser.read()
        return robot_parser.can_fetch(user_agent, base_url)

    def scrape_tech_news(self):
        base_url = "https://techcrunch.com/"


        if not self.is_scraping_allowed(base_url):
            self.stdout.write(self.style.WARNING("Scraping is not allowed by robots.txt."))
            return

        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Uncomment for headless mode
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        try:
            driver.get(base_url)
            time.sleep(5)  # Adjust as needed
            page_content = driver.page_source
            soup = BeautifulSoup(page_content, 'html.parser')
            news_articles = soup.find_all('li', class_='wp-block-post')

            if not news_articles:
                self.stdout.write(self.style.WARNING("No articles found."))
                return

            for article in news_articles:
                try:
                    title_element = article.find('h3', class_='loop-card__title')
                    link_element = title_element.find('a', class_='loop-card__title-link') if title_element else None
                    image_element = article.find('img')
                    content_element= article.find("p", class_='loop-card__detail')

                    title = title_element.get_text(strip=True) if title_element else "No title found"
                    link = link_element['href'] if link_element else "No link found"
                    image_url = image_element['src'] if image_element else "No image found"
                    content = content_element.get_text(strip=True) if content_element else "use the link to view"
                    # Truncate the title if it exceeds 200 characters
                    if len(title) > 200:
                        title = title[:50]

                    # if len(image_url) > 500:
                    

                    # Ensure slug is unique
                    slug = slugify(title)
                    existing_news = News.objects.filter(slug=slug).first()
                    if existing_news:
                        self.stdout.write(self.style.WARNING(f"Skipping duplicate news item: {title}"))
                        continue

                    # Handle news category
                    category, created = NewsCategory.objects.get_or_create(title="Tech News")
                    
                    #downloader downloads image from url to s3bucket
                    
                    news_item = News.objects.create(
                        title=title,
                        slug=slug,
                        content="",  # You can customize this based on your needs
                       
                        news_category=category,
                        news_source="TechCrunch",
                        external_link = link
                        
                    )
                    
                    image_downloader.save_image_from_url(image_url, news_item)

                    news_item.save()
                    try:
                        self.stdout.write(self.style.SUCCESS(f"Saved: {news_item.title}"))
                        # Your code to save the article data
                    except IntegrityError as e:
                        print(f"Error saving article: {e}")


                    

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error extracting article data: {e}"))
                    continue
                from django.db import IntegrityError

               
        except (WebDriverException, TimeoutException, IntegrityError ) as e:
            self.stdout.write(self.style.ERROR(f"Error loading the page: {e}"))
        finally:
            driver.quit()
