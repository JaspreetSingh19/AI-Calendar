"""
This file contains serializers related to 'meetings' model
for scheduling meetings
"""
from django.db.models import Q
from rest_framework import serializers

from common.constants import MIN_LENGTH, MAX_LENGTH
from common.messages import VALIDATION
from meetings.models import Meetings


class MeetingsListSerializer(serializers.ModelSerializer):
    """
    MeetingsListSerializer for getting list of meetings
    """
    from_user = serializers.StringRelatedField()
    to_user = serializers.StringRelatedField()

    class Meta:
        """
        Use the Meta class to specify the model and fields
        that the MeetingsListSerializer should work with
        """
        model = Meetings
        fields = ['id', 'from_user', 'to_user', 'title', 'start_time', 'end_time', 'created_at', 'updated_at']


class MeetingsCreateSerializer(serializers.ModelSerializer):
    """
    MeetingsCreateSerializer for creating a new meeting
    """
    title = serializers.CharField(min_length=MIN_LENGTH['title'], max_length=MAX_LENGTH['title'], required=True)
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()

    def validate(self, attrs):
        """
        Validation to check there are meeting conflicts
        :param attrs: from_user,to_user
        :return: validation message, attrs
        """
        from_user = self.context['user'].id
        to_user = attrs.get('to_user')
        start_time = attrs.get('start_time')
        end_time = attrs.get('end_time')

        conflict_query = (
                Q(from_user=from_user, start_time__lte=end_time, end_time__gte=start_time) |
                Q(to_user=to_user, start_time__lte=end_time, end_time__gte=start_time)
        )

        if Meetings.objects.filter(conflict_query).exists():
            raise serializers.ValidationError({'meeting': VALIDATION['meeting_conflicts']})

        return attrs

    def create(self, validated_data):
        """
        Override create() method to create a new meeting
        """
        from_user = self.context['user']

        meeting = Meetings.objects.create(from_user=from_user, to_user=validated_data['to_user'],
                                          title=validated_data['title'], start_time=validated_data['start_time'],
                                          end_time=validated_data['end_time'])
        return meeting

    class Meta:
        """
        Use the Meta class to specify the model and fields
        that the MeetingsCreateSerializer should work with
        """
        model = Meetings
        fields = ['id', 'to_user', 'title', 'start_time', 'end_time', 'created_at', 'updated_at']
