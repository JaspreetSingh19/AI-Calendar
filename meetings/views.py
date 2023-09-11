"""
This file contains different ViewSet for 'Meetings'
The MeetingsViewSet handles CRUD operations for the Meetings model.
"""
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.constants import CREATE
from common.messages import SUCCESS_MESSAGES
from common.permissions import UserCanDeleteMeeting
from meetings.models import Meetings
from meetings.serializers import MeetingsListSerializer, MeetingsCreateSerializer


class MeetingsViewSet(viewsets.ModelViewSet):
    """
    The MeetingsViewSet handles 'create', 'delete' operations for the Meetings model,
    It provides a serializer class for each action with permission class
    """
    http_method_names = ['get', 'post', 'delete']
    queryset = Meetings
    serializer_class = MeetingsListSerializer
    serializer_create_class = MeetingsCreateSerializer
    permission_classes = (IsAuthenticated, UserCanDeleteMeeting)

    def get_queryset(self):
        """
        The get_queryset method returns a queryset of Meetings Model objects
        It orders the queryset based on the created_at of the objects.
        :return: Meeting objects
        """
        user = self.request.user.id
        queryset = self.queryset.objects.filter(Q(from_user=user) | Q(to_user=user)).order_by('created_at')
        return queryset

    def get_serializer_class(self):
        """
        The get_serializer_class returns a serializer class based on the action being performed.
        For 'create' action, it returns MeetingsCreateSerializer,
        and for all other actions, it returns the default serializer, MeetingsListSerializer.
        :return: serializer class
        """
        if self.action == CREATE:
            return self.serializer_create_class
        return self.serializer_class

    def list(self, request, *args, **kwargs):
        """
        The list retrieves all instances of the Meetings model.
        serializes them using the serializer returned by the get_serializer() method,
        and returns the serialized data in a Response object with a status code of 200 (OK).
        :return: Meeting instances
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        This method retrieves a single instance of the Meetings model
        using the provided primary key (pk).
        It then serializes the instance using the serializer defined for the view and
        returns the serialized data in a Response object with a status code of 200 (OK).
        :return: Single Meetings instance
        """
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        This method creates a new instance of the Meetings model using validated serializer data
        If the data is valid, it creates a new instance and
        returns a success response with a status code of 201.
        If the data is invalid, it returns an error response with a status code of 400.
        :return: Meetings object
        """
        serializer = self.get_serializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            meeting = serializer.create(serializer.validated_data)
            response_serializer = self.serializer_class(meeting)
            return Response({'message': SUCCESS_MESSAGES['meeting']['created'],
                             'data': response_serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        This method deletes an instance of the Meetings model using the primary key
        It returns a success response with a message after the deletion is complete.
        :return: success response
        """
        instance = self.get_object()
        instance.delete()
        return Response({'message': SUCCESS_MESSAGES['meeting']['deleted']}, status=status.HTTP_200_OK)
