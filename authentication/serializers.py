"""
This file contains serializers for authentication purposes
"""
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import User
from common.constants import MIN_LENGTH, MAX_LENGTH
from common.messages import VALIDATION


class LoginSerializer(serializers.ModelSerializer):
    """
    used to verify the login credentials and return the login response
    """
    email = serializers.EmailField(
        required=True, allow_blank=False, error_messages=VALIDATION['email']
    )
    password = serializers.CharField(
        min_length=MIN_LENGTH['password'], max_length=MAX_LENGTH['password'], write_only=True, required=True,
        trim_whitespace=False, error_messages=VALIDATION['password']
    )

    def validate(self, attrs):
        """
        Validation to check user credentials
        :param attrs: email, password
        :return: validation message or attrs
        """
        email = attrs.get('email')
        password = attrs.get('password')

        user = User.objects.filter(email=email).first()

        if not user:
            raise serializers.ValidationError({'credentials': VALIDATION['invalid_credentials']})

        if not user.check_password(password):
            raise serializers.ValidationError({'credentials': VALIDATION['invalid_credentials']})

        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        """
        Generate the access and refresh tokens for the authenticated user
        """
        user = User.objects.filter(email=validated_data['email']).first()
        refresh = RefreshToken.for_user(user)

        user_token = User.objects.get(id=user.id)
        user_token.token = str(refresh.access_token)
        user_token.save()

        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

    class Meta:
        """
         Metaclass to specify model login serializer
         should work with
        """
        model = User
        fields = ['email', 'password']
