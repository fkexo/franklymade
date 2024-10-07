from django.urls import path
from .views import NewsArticleListCreate

urlpatterns = [
    path('articles/', NewsArticleListCreate.as_view(), name='news_article_list_create'),
]
