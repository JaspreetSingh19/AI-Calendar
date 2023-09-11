"""
This file contains user admin for registering models
in the django admin panel
"""
from django.contrib import admin

from account.models import User


class UserAdmin(admin.ModelAdmin):
    """
    User admin for 'user' model
    """
    list_display = (
        'id', 'first_name', 'last_name', 'email', 'contact', 'created_at', 'updated_at'
    )

    class Meta:
        """
        Metaclass to specify model
        UserAdmin should work with
        """
        model = User


admin.site.register(User, UserAdmin)
