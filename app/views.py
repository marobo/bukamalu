"""
Views for location sharing.
"""
import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import LocationSession


def home(request):
    """Home page with the share button."""
    return render(request, 'home.html')


@csrf_exempt
@require_http_methods(["POST"])
def create_session(request):
    """Create a new location sharing session."""
    try:
        data = json.loads(request.body)
        lat = data.get('lat')
        lng = data.get('lng')
        
        if lat is None or lng is None:
            return JsonResponse({'error': 'Location required'}, status=400)
        
        # Create new session
        session = LocationSession.objects.create(
            host_lat=lat,
            host_lng=lng
        )
        session.host_last_update = session.created_at
        session.save(update_fields=['host_last_update'])
        
        # Build the share URL
        share_url = request.build_absolute_uri(f'/share/{session.session_code}')
        
        return JsonResponse({
            'success': True,
            'session_code': session.session_code,
            'share_url': share_url
        })
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)


def share_page(request, session_code):
    """Page for viewing the shared location (visitor view)."""
    session = get_object_or_404(LocationSession, session_code=session_code)
    
    # Check if session is expired or inactive
    is_valid = session.is_active and not session.is_expired()
    
    return render(request, 'share.html', {
        'session_code': session_code,
        'is_valid': is_valid,
        'host_lat': session.host_lat,
        'host_lng': session.host_lng,
    })


def host_page(request, session_code):
    """Page for the host to view the map after sharing."""
    session = get_object_or_404(LocationSession, session_code=session_code)
    
    is_valid = session.is_active and not session.is_expired()
    
    return render(request, 'host.html', {
        'session_code': session_code,
        'is_valid': is_valid,
        'host_lat': session.host_lat,
        'host_lng': session.host_lng,
    })


@csrf_exempt
@require_http_methods(["POST"])
def update_location(request, session_code):
    """Update location for either host or visitor."""
    session = get_object_or_404(LocationSession, session_code=session_code)
    
    # Check if session is still active
    if not session.is_active or session.is_expired():
        return JsonResponse({'error': 'Session expired'}, status=410)
    
    try:
        data = json.loads(request.body)
        lat = data.get('lat')
        lng = data.get('lng')
        role = data.get('role', 'visitor')  # 'host' or 'visitor'
        
        if lat is None or lng is None:
            return JsonResponse({'error': 'Location required'}, status=400)
        
        if role == 'host':
            session.update_host_location(lat, lng)
        else:
            session.update_visitor_location(lat, lng)
        
        return JsonResponse({'success': True})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)


@require_http_methods(["GET"])
def get_locations(request, session_code):
    """Get current locations for both host and visitor."""
    session = get_object_or_404(LocationSession, session_code=session_code)
    
    # Check if session is still active
    if not session.is_active or session.is_expired():
        return JsonResponse({
            'error': 'Session expired',
            'is_active': False
        }, status=410)
    
    return JsonResponse(session.get_locations())


@csrf_exempt
@require_http_methods(["POST"])
def stop_session(request, session_code):
    """Stop the sharing session."""
    session = get_object_or_404(LocationSession, session_code=session_code)
    session.deactivate()
    return JsonResponse({'success': True})
