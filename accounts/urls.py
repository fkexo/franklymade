from django.urls import path
from . import views



urlpatterns = [
    path('dashboard', views.dashbaord, name='dashboard' ),
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),

    path('contribute', views.contributePost, name='contribute'),

    
    
]
