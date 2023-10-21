from django.db import models
from django.contrib.auth.models import User
from enumchoicefield import ChoiceEnum, EnumChoiceField
from common.TimestampsMixins import TimestampsMixin

from itinerary.models import Itinerary


class ExperienceTypes(ChoiceEnum):
    EATERY = "eatery"
    EXPERIENCE = "experience"
    MONUMENT = "monument"
    OTHER = "other"

    def __str__(self):
        return self.value


class Experience(TimestampsMixin):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=180)
    type = EnumChoiceField(ExperienceTypes, default=ExperienceTypes.OTHER)
    google_place_id = models.CharField(max_length=120, null=True)
    ticket_link = models.CharField(max_length=180, blank=True, null=True)
    reservation_link = models.CharField(max_length=180, blank=True, null=True)
    activity_start_time = models.DateTimeField(blank=True, null=True)
    activity_end_time = models.DateTimeField(blank=True, null=True)

    # Itinerary
    order = models.IntegerField(null=False)
    itinerary = models.ForeignKey(
        Itinerary, on_delete=models.CASCADE, related_name="experiences"
    )

    # User Info
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("order", "itinerary")
