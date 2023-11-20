from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('article/<int:article_id>', views.viewBlog, name='myarticle'),
    path('about', views.about_blog, name='about_blog'),

]


