import re

from rest_framework import serializers

from account.models import User
from common.constants import MAX_LENGTH, MIN_LENGTH, REGEX
from common.messages import VALIDATION


class RegistrationSerializer(serializers.ModelSerializer):
    """
    serializer for Registering requested user
    """

    first_name = serializers.CharField(
        max_length=MAX_LENGTH['first_name'], min_length=MIN_LENGTH['first_name'], required=True, allow_blank=False,
        trim_whitespace=True, error_messages=VALIDATION['first_name']
    )
    last_name = serializers.CharField(
        max_length=MAX_LENGTH['last_name'], min_length=MIN_LENGTH['last_name'], required=True, allow_blank=False,
        trim_whitespace=False, error_messages=VALIDATION['last_name']
    )
    email = serializers.EmailField(
        required=True, allow_blank=False, error_messages=VALIDATION['email']
    )
    contact = serializers.CharField(
        min_length=MIN_LENGTH['contact'], max_length=MAX_LENGTH['contact'], required=True, allow_blank=False,
        error_messages=VALIDATION['contact']
    )
    password = serializers.CharField(
        write_only=True, min_length=MIN_LENGTH['password'], max_length=MAX_LENGTH['password'], required=True,
        allow_blank=False, error_messages=VALIDATION['password']
    )
    confirm_password = serializers.CharField(
        write_only=True, min_length=MIN_LENGTH['password'], max_length=MAX_LENGTH['password'], required=True,
        allow_blank=False, error_messages=VALIDATION['password']
    )

    def validate(self, attrs):
        """
        Validation to check if password and confirm password mathces
        :param attrs: password, confirm password
        :return: validation message or attrs
        """
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({'password': VALIDATION['password']['do_not_match']})

        return attrs

    @staticmethod
    def validate_first_name(value):
        """
        check that the first_name should contain only alphabets
        :param value:first_name
        :return:if valid return value ,else return Validation error
        """
        if not re.match(REGEX["first_name"], value):
            raise serializers.ValidationError(VALIDATION['first_name']['invalid'])
        return value

    @staticmethod
    def validate_last_name(value):
        """
        check that the last_name should contain only alphabets
        :param value:last_name
        :return:if valid return value ,else return Validation error
        """
        if not re.match(REGEX["last_name"], value):
            raise serializers.ValidationError(VALIDATION['last_name']['invalid'])
        return value

    @staticmethod
    def validate_email(value):
        """
        check that the last_name should contain only alphabets
        :param value:email
        :return:if valid return value ,else return Validation error
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(VALIDATION['email']['exists'])
        return value

    @staticmethod
    def validate_contact(value):
        """
        check that the contact should contain only digits
        :param value:contact
        :return:if valid return value ,else return Validation error
        """
        if not re.match(REGEX["contact"], value):
            raise serializers.ValidationError(VALIDATION['contact']['invalid'])
        if User.objects.filter(contact=value).exists():
            raise serializers.ValidationError(VALIDATION['contact']['exists'])
        return value

    @staticmethod
    def validate_password(value):
        """
        checks password if valid : return value,
        else : return validation error
        """
        if not re.match(REGEX["password"], value):
            raise serializers.ValidationError(VALIDATION['password']['invalid'])
        return value

    def create(self, validated_data):
        """
        Override create() method to create a new user
        """
        validated_data.pop('confirm_password')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        """
        Metaclass to specify model
        Registration serializer should work with
        """
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'contact', 'password', 'confirm_password']
