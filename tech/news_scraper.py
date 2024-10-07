import requests
from bs4 import BeautifulSoup
from datetime import datetime


#******************** to be able to import the models
import sys
import os
from django.conf import settings

# Add the project base directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'franklymade.settings')

# Import Django setup
import django
django.setup()

from tech.models import News  # Now the import should work


def scrape_tech_news():
    url = 'https://techcrunch.com/'  # Change this URL to your preferred tech news site
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Adjust the selectors based on the website structure
        articles = soup.find_all('h2', class_='post-title')  # Example selector for TechCrunch
        
        for article in articles:
            title = article.get_text(strip=True)
            link = article.find('a')['href']

            # Create a description or fetch additional data if needed
            description = "Auto-scraped from TechCrunch"
            pub_date = datetime.now()  # You can replace this with the actual published date if available

            # Check if this news already exists to avoid duplicates
            if not News.objects.filter(title=title).exists():
                News.objects.create(
                    title=title,
                    link=link,
                    description=description,
                    pup_date=pub_date
                )
                print(f'Successfully added: {title}')
            else:
                print(f'News already exists: {title}')
    else:
        print(f'Failed to retrieve news: {response.status_code}')

# Call the function
scrape_tech_news()
