"""
Models for location sharing sessions.
"""
import secrets
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.conf import settings


def generate_session_code():
    """Generate a unique 8-character session code."""
    return secrets.token_urlsafe(6)


class LocationSession(models.Model):
    """
    Represents a location sharing session between a host and visitor.
    """
    session_code = models.CharField(
        max_length=20,
        unique=True,
        default=generate_session_code,
        db_index=True
    )
    
    # Host location
    host_lat = models.FloatField(null=True, blank=True)
    host_lng = models.FloatField(null=True, blank=True)
    host_last_update = models.DateTimeField(null=True, blank=True)
    
    # Visitor location
    visitor_lat = models.FloatField(null=True, blank=True)
    visitor_lng = models.FloatField(null=True, blank=True)
    visitor_last_update = models.DateTimeField(null=True, blank=True)
    
    # Session state
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Session {self.session_code}"
    
    def is_expired(self):
        """Check if the session has expired."""
        expiry_hours = getattr(settings, 'LOCATION_SESSION_EXPIRY_HOURS', 2)
        expiry_time = self.created_at + timedelta(hours=expiry_hours)
        return timezone.now() > expiry_time
    
    def update_host_location(self, lat, lng):
        """Update host's location."""
        self.host_lat = lat
        self.host_lng = lng
        self.host_last_update = timezone.now()
        self.save(update_fields=['host_lat', 'host_lng', 'host_last_update'])
    
    def update_visitor_location(self, lat, lng):
        """Update visitor's location."""
        self.visitor_lat = lat
        self.visitor_lng = lng
        self.visitor_last_update = timezone.now()
        self.save(update_fields=['visitor_lat', 'visitor_lng', 'visitor_last_update'])
    
    def deactivate(self):
        """Stop the sharing session."""
        self.is_active = False
        self.save(update_fields=['is_active'])
    
    def get_locations(self):
        """Get both locations as a dictionary."""
        return {
            'host': {
                'lat': self.host_lat,
                'lng': self.host_lng,
                'last_update': self.host_last_update.isoformat() if self.host_last_update else None
            },
            'visitor': {
                'lat': self.visitor_lat,
                'lng': self.visitor_lng,
                'last_update': self.visitor_last_update.isoformat() if self.visitor_last_update else None
            },
            'is_active': self.is_active and not self.is_expired()
        }
