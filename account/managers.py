"""
This file contains manager for User model
"""
from django.contrib.auth.models import UserManager


class UserBaseManager(UserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user with the given email and password.

        :param email: The email address of the user (required)
        :param password: The password of the user (optional)
        :param extra_fields: Any additional fields to be saved for the user (optional)
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user with the given email and password.

        :param email: The email address of the user (required)
        :param password: The password of the user (optional)
        :param extra_fields: Any additional fields to be saved for the user (optional)
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)
