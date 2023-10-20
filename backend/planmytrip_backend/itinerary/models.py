from django.db import models
from django.contrib.auth.models import User
from common.TimestampsMixins import TimestampsMixin


class Itinerary(TimestampsMixin):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=180)
    timeline = models.JSONField(default=list)

    # User Info
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
