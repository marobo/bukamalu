"""Template context processors."""
from django.conf import settings


def mapbox_token(request):
    """Expose Mapbox access token to templates for map tiles."""
    return {'mapbox_token': getattr(settings, 'MAPBOX_ACCESS_TOKEN', '')}


def language_switcher(request):
    """Expose path without language prefix and LANGUAGES for building switch links."""
    path = request.path.strip('/')
    parts = path.split('/', 1)
    # First segment is language code when using i18n_patterns
    path_without_lang = parts[1] if len(parts) > 1 else ''
    return {
        'path_without_lang': path_without_lang,
        'LANGUAGES': settings.LANGUAGES,
    }
