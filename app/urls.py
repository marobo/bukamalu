"""
URL patterns for location sharing app.
"""
from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path('', views.home, name='home'),
    path('share/<str:session_code>', views.share_page, name='share_page'),
    path('host/<str:session_code>', views.host_page, name='host_page'),
    
    # API endpoints
    path('api/create-session', views.create_session, name='create_session'),
    path('api/update/<str:session_code>', views.update_location, name='update_location'),
    path('api/locations/<str:session_code>', views.get_locations, name='get_locations'),
    path('api/stop/<str:session_code>', views.stop_session, name='stop_session'),
]
