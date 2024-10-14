
from django.urls import path
from . import views

#  title = post.course_category
urlpatterns = [
    path('', views.index, name='index'),
    path('tech_update', views.techHome, name='tech_home'),
    path('tech_update/<slug:slug>', views.detailPage, name='detail_page'),
    path('add_tech_news', views.addTechNews, name = 'add_tech_news'),

    # tech news category item list 
    path('categories/', views.news_category_list, name='news_category_list'),  # All categories
    path('category/<slug:category_slug>/', views.news_by_category, name='news_by_category'),  # News by category
    # path('news/<slug:slug>/', views.news_detail, name='news_detail'),  # Specific news item detail


    
]


from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )

