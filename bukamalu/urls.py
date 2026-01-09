"""
URL configuration for Bukamalu project.
"""
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
]
