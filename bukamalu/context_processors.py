"""Template context processors."""
from django.conf import settings


def mapbox_token(request):
    """Expose Mapbox access token to templates for map tiles."""
    return {'mapbox_token': getattr(settings, 'MAPBOX_ACCESS_TOKEN', '')}
