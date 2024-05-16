from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogHome, name='blog_home'),
    
    path('article/<slug:slug>', views.viewBlog, name='myarticle'),
    path('add_article/', views.addArticle, name='add_article'),


]


