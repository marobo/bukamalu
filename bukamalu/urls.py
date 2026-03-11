"""
URL configuration for Bukamalu project.
"""

from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings


urlpatterns = i18n_patterns(
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += i18n_patterns(
        path('rosetta/', include('rosetta.urls')),
    )
