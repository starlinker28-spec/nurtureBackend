from django.contrib import admin
from django.urls import path, include  # <-- FIX 1: Corrected typo

# Import the correct view for Google Sign-In
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

# Define the view that will handle our Google login
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://localhost' # Dummy URL, but required

urlpatterns = [
    # This file's URLs are already prefixed with 'api/' 
    # so we just add the paths *inside* 'api/'.
    
    # We remove the old circular import.
    
    # CRITICAL FIX:
    # Our custom Google login URL must be *before* the default auth URLs.
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),

    # This line provides the other default dj-rest-auth endpoints
    # It will be at /api/auth/
    path('auth/', include('dj_rest_auth.urls')),
    
    # You can add other app-specific URLs here, for example:
    # path('posts/', ...),
    # path('profile/', ...),
]