from django.urls import path
from . import views

#  title = post.course_category
urlpatterns = [
    # page for all the course categories
    
    path('Learn-to-code', views.tutorial_home, name='tutorial_home'), 
    path('<id>/courses', views.course_series, name='course_series_list'), 
    path('course<id>/', views.course_detail, name='course_detail'), 

    path('lessons', views.my_lesson_list, name='lesson_list' ),

    path('lesson/<slug:slug>', views.lessonContent, name='lesson' ),
    path('add-lesson', views.addLesson, name='add_lesson' ),
    

    # path('pythontutorial', views.python_intro, name='python_intro'),
    # path('lesson/<slug:slug>', views.python_cours_details, name='courses'),
    # # path('lesson/<int:course_id>', views.python_cours_details, name='courses'),
    # path('learnDejango', views.django_intro, name='django_intro' ),
    # path('search', views.searchBar, name='searchitem' ),

    # new created url for the create course and course details functions
    
    # path('course/<slug:slug>', views.courseDetail, name='course' ),
    
    
    
    
]


from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )

