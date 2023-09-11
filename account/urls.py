"""
This file contains URL patterns for account
It uses a DefaultRouter to generate views
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.views import RegistrationViewSet

router = DefaultRouter()


router.register('registration', RegistrationViewSet, basename='registration')


urlpatterns = [
    path('', include(router.urls)),
]
