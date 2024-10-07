from django.core.management.base import BaseCommand
import scrape_tech_news  # Adjust the import based on your structure


class Command(BaseCommand):
    help = 'Scrapes the latest tech news from TechCrunch'

    def handle(self, *args, **kwargs):
        scrape_tech_news()



