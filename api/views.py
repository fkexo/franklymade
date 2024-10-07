from django.shortcuts import render
from api.models import NewsArticle
# Create your views here.
from rest_framework import generics
from .models import NewsArticle
from .serializers import NewsArticleSerializer

class NewsArticleListCreate(generics.ListCreateAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer


# this goes into the scraping function to write into the database
# # Inside your scraping function, after getting the title, link, and image_url
# from api.models import NewsArticle
# NewsArticle.objects.update_or_create(
#     title=title,
#     defaults={'link': link, 'image_url': image_url}
# )

# Access the API
# we can access the API at http://127.0.0.1:8000/api/articles/ to see the articles and also to post new articles.


