"""
Django settings for Bukamalu - Two-Way Location Sharing project.
"""

from pathlib import Path

from django.conf import locale
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'visitor_stats',
    'app',
    'rosetta',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'visitor_stats.middleware.VisitorTrackingMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROOT_URLCONF = 'bukamalu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bukamalu.context_processors.mapbox_token',
                'bukamalu.context_processors.language_switcher',
            ],
        },
    },
]

WSGI_APPLICATION = 'bukamalu.wsgi.application'

# Database - using SQLite for simplicity
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dili'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('tet', 'Tetum'),
    ('en', 'English'),
]

# Add extra languages not provided by Django
EXTRA_LANG_INFO = {
    'tet': {
        'bidi': False,
        'code': 'tet',
        'name': 'Tetum',
        'name_local': 'Tetum',
    }
}

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Add custom languages not provided by Django
locale.LANG_INFO.update(EXTRA_LANG_INFO)

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Session expiry time in hours
LOCATION_SESSION_EXPIRY_HOURS = 2

# Mapbox: set MAPBOX_ACCESS_TOKEN in .env to use Mapbox tiles (otherwise OSM/Esri)
MAPBOX_ACCESS_TOKEN = config('MAPBOX_ACCESS_TOKEN', default='')

try:
    from .local_settings import *
except ImportError:
    pass
