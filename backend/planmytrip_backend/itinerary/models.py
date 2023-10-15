from django.db import models
from django.contrib.auth.models import User


class Itinerary(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=180)

    # User Info
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    # Metadata
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name
