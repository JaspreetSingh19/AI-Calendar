"""
This file contains meeting admin for registering models
in the django admin panel
"""
from django.contrib import admin

from meetings.models import Meetings


class MeetingsAdmin(admin.ModelAdmin):
    """
    Meetings admin for 'meetings' model
    """
    list_display = (
        'id', 'from_user', 'to_user', 'title', 'start_time', 'end_time', 'created_at', 'updated_at'
    )

    class Meta:
        """
        Metaclass to specify model
        MeetingsAdmin should work with
        """
        model = Meetings


admin.site.register(Meetings, MeetingsAdmin)
