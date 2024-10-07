from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from urllib.robotparser import RobotFileParser
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

# Path to your WebDriver (e.g., ChromeDriver)
driver_path = r"C:\chromedriver-win64\chromedriver.exe"  # Ensure the path is correct

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

    driver = None  # Initialize driver variable
    try:
        # Create a Service object
        service = Service(driver_path)
        
        # Initialize the WebDriver using the Service
        driver = webdriver.Chrome(service=service)
        
        # Open the page
        driver.get(base_url)

        # Wait for the page to fully load
        time.sleep(5)  # Rate-limiting, wait for 5 seconds (adjust if needed)

        # Extract the page source after JavaScript has rendered the content
        page_content = driver.page_source
        print(page_content)

        # Use BeautifulSoup to parse the now-rendered HTML
        soup = BeautifulSoup(page_content, 'html.parser')

        # Find the news articles based on <h2> tags, adjust the selector as needed
        news_articles = soup.find_all('h2')  # Consider all <h2> tags or specify a class

        # Error handling if no articles found
        if not news_articles:
            print("No articles found.")
            return []

        # Extract the news titles and links
        for article in news_articles:
            try:
                title = article.get_text(strip=True)
                link = article.find('a')['href'] if article.find('a') else "No link found"
                print(f"Title: {title}, Link: {link}")
            except AttributeError:
                print("Error extracting article data.")
                continue

    except (WebDriverException, TimeoutException) as e:
        print(f"Error loading the page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the WebDriver
        if driver:
            driver.quit()

# Call the function
scrape_tech_news()
