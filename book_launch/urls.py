"""
URL configuration for book_launch project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Redirect default Django admin to custom admin login
    path('admin/', RedirectView.as_view(pattern_name='admin_login', permanent=False)),
    path('', include('visitors.urls')),
]
