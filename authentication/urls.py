"""
This file contains URL patterns for authentication
It uses a DefaultRouter to generate views
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authentication.views import LoginViewSet

router = DefaultRouter()


router.register('login', LoginViewSet, basename='login')


urlpatterns = [
    path('', include(router.urls)),
]
