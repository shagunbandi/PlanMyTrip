from django.db import models
from django.contrib.auth.models import User
from enumchoicefield import ChoiceEnum, EnumChoiceField
from common.mixins.TimestampsMixin import TimestampsMixin
from common.mixins.ReservationMixin import ReservationMixin

from itinerary.models import Itinerary


class ExperienceTypes(ChoiceEnum):
    EATERY = "eatery"
    EXPERIENCE = "experience"
    MONUMENT = "monument"
    OTHER = "other"

    def __str__(self):
        return self.value


class Experience(TimestampsMixin, ReservationMixin):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=180)
    type = EnumChoiceField(ExperienceTypes, default=ExperienceTypes.OTHER)

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
