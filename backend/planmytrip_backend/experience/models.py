from django.db import models
from django.contrib.auth.models import User
from enumchoicefield import ChoiceEnum, EnumChoiceField


class ExperienceTypes(ChoiceEnum):
    EATERY = "eatery"
    EXPERIENCE = "experience"
    MONUMENT = "monument"
    OTHER = "other"


class Experience(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=180)
    type = EnumChoiceField(ExperienceTypes, default=ExperienceTypes.OTHER)
    google_place_id = models.CharField(max_length=120, null=True)
    ticket_link = models.CharField(blank=True, null=True)
    reservation_link = models.CharField(blank=True, null=True)
    activity_start_time = models.DateTimeField(blank=True, null=True)
    activity_end_time = models.DateTimeField(blank=True, null=True)

    # User Info
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    # Metadata
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name
