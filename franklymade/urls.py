
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('tech.urls')),

     path('api/', include('api.urls')),

    path('accounts/', include('accounts.urls')),
    
    path('courses/', include('tutorial.urls')),
    path('blog/', include('blog.urls')),
    path('franklin/', include('portinfo.urls')),
    
]





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )

