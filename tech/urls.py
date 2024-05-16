
from django.urls import path
from . import views

#  title = post.course_category
urlpatterns = [
    path('', views.index, name='index'),
    path('tech_update', views.techHome, name='tech_home'),
    path('tech_update/<slug:slug>', views.detailPage, name='detail_page'),
    path('add_tech_news', views.addTechNews, name = 'add_tech_news')

    
]


from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )

