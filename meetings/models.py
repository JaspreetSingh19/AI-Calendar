"""
This file contains model for scheduling meetings
"""
from django.db import models

from account.models import User
from common.models import TimeStampedModel


class Meetings(TimeStampedModel):
    """
    Meeting model for representing meetings with different users
    and with fk
    """
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    objects = models.Manager()

    def __str__(self):
        """
        String representation for meeting model
        :return: title of meeting
        """
        return self.title

    class Meta:
        """
        Use the Meta class to specify the database table
        for Meetings model
        """
        db_table = 'meetings'
