from django import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('config.router')),
]
