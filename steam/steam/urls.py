from django.contrib import admin
from django.urls import path, include
from .settings import local as settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls')),
    path('users/', include('users.urls')),
    path('api/', include('api.routers')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
