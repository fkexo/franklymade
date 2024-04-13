from django.urls import path
from . import views

#  title = post.course_category
urlpatterns = [
    path('', views.franklymade_home, name='franklymade'),
    path('pythontutorial', views.python_intro, name='python_intro'),
    path('lesson/<slug:slug>', views.python_cours_details, name='courses'),
    # path('lesson/<int:course_id>', views.python_cours_details, name='courses'),
    path('learnDejango', views.django_intro, name='django_intro' ),
    path('search', views.searchBar, name='searchitem' ),

    # new created url for the create course and course details functions
    path('create_course', views.create_course, name='create_course' ),
    path('course/<slug:slug>', views.courseDetail, name='course' ),
    
    
]


from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )

