from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from urllib.robotparser import RobotFileParser
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'franklymade.settings')
django.setup()

from tech.models import News, NewsCategory
from django.utils.text import slugify

# Define your scraping logic
def is_scraping_allowed(base_url, user_agent="*"):
    """
    Check if scraping is allowed by robots.txt.
    """
    robots_url = f"{base_url}/robots.txt"
    robot_parser = RobotFileParser()
    robot_parser.set_url(robots_url)
    robot_parser.read()
    
    # Check if user agent is allowed to scrape the base_url
    return robot_parser.can_fetch(user_agent, base_url)

def scrape_tech_news():
    base_url = "https://techcrunch.com/"
    
    # Check robots.txt to ensure scraping is allowed
    if not is_scraping_allowed(base_url):
        print("Scraping is not allowed by robots.txt.")
        return

    driver = None  # Initialize driver as None before the try block
    try:
        # Initialize the WebDriver using ChromeDriverManager
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Uncomment for headless mode
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        
        # Open the page
        driver.get(base_url)

        # Wait for the page to fully load
        time.sleep(5)  # Adjust the sleep time if necessary

        # Extract the page source after JavaScript has rendered the content
        page_content = driver.page_source

        # Use BeautifulSoup to parse the now-rendered HTML
        soup = BeautifulSoup(page_content, 'html.parser')

        # Find the news articles based on the <li> tag structure
        news_articles = soup.find_all('li', class_='wp-block-post')

        # Error handling if no articles found
        if not news_articles:
            print("No articles found.")
            return []

        # Extract the news titles and links
        for article in news_articles:
            try:
                title_element = article.find('h3', class_='loop-card__title')
                link_element = title_element.find('a', class_='loop-card__title-link') if title_element else None
                image_element = article.find('img') 

                # Extract data
                title = title_element.get_text(strip=True) if title_element else "No title found"
                link = link_element['href'] if link_element else "No link found"
                image_url = image_element['src'] if image_element else "No image found"
                content = f"Read the full article at {link}"  # Placeholder for content as we're not scraping the full article text
                category_title = "Tech"  # You can update this or scrape categories if available
                news_source = "TechCrunch"
                featured_post = False  # Set this based on your logic or random assignment

                # Print extracted data for debugging
                print(f"Title: {title}, Link: {link}, Image URL: {image_url}")

                # Save to database
                # Get or create the news category
                category, created = NewsCategory.objects.get_or_create(title=category_title)

                # Create or update the News entry
                news_entry, created = News.objects.update_or_create(
                    title=title,
                    defaults={
                        'content': content,
                        'news_image': image_url,
                        'slug': slugify(title),
                        'news_category': category,
                        'news_source': news_source,
                        'featured_post': featured_post,
                    }
                )

                print(f"Saved article: {news_entry.title}")

            except AttributeError as e:
                print(f"Error extracting article data: {e}")
                continue

    except (WebDriverException, TimeoutException) as e:
        print(f"Error loading the page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the WebDriver if it was initialized
        if driver is not None:
            driver.quit()

# Call the function
scrape_tech_news()
