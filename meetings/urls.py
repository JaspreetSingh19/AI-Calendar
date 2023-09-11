"""
This file contains URL patterns for meeting
It uses a DefaultRouter to generate views
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from meetings.views import MeetingsViewSet

router = DefaultRouter()


router.register('meetings', MeetingsViewSet, basename='meetings')


urlpatterns = [
    path('', include(router.urls)),
]
