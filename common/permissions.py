"""
This file contains custom permissions which can be used throughout the project
"""
from rest_framework import permissions


class UserCanDeleteMeeting(permissions.BasePermission):
    """
    Custom permission to allow only the 'from_user' of a meeting to delete it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user making the request is the 'from_user' of the meeting.
        """
        return obj.from_user == request.user
