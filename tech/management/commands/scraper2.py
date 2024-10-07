import requests
from bs4 import BeautifulSoup
import time

# URL of the site to scrape
url = "https://techcrunch.com/"  # Update with the actual page for the latest tech news

def scrape_tech_news():
    # Set headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Request the page
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an exception for non-200 status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    # Parse the content
    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')

    # Debug: Print the first 500 characters of the page to ensure we are getting content
    print(page_content[:500])

    # Locate the <h2> elements with the specific ID or class
    news_articles = soup.find_all('h2', id='h-latest-news')  # Using 'id' to target the correct node

    # Check if articles are found
    if not news_articles:
        print("No articles found with the given ID.")
        return []

    # Parse and extract the news titles and links
    for article in news_articles:
        title = article.get_text(strip=True)
        # Assuming the link is inside an anchor tag within the <h2> tag
        link = article.find('a')['href'] if article.find('a') else "No link found"
        print(f"Title: {title}, Link: {link}")

    return news_articles

# Call the function
scrape_tech_news()
