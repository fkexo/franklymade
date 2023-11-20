from django.urls import path
from . import views


urlpatterns = [
    path('', views.franklymade_home, name='franklymade'),
    path('pythontutorial', views.python_intro, name='python_intro'),
    path('lesson/<int:course_id>', views.python_cours_details, name='courses'),
    path('learnDejango', views.django_intro, name='django_intro' ),
    path('search', views.searchBar, name='searchitem' ),






]
