from django.urls import path
from . import views


urlpatterns = [
    path('', views.portinfo_home, name='portinfo'),
    path('projects', views.allProjects, name='projects'),
    path('details', views.projectDetails, name='details'),
    # path('contact-me', views.contact_me, name='contact-me'),
    # path('contact', views.contactMe, name='contact'),

]
