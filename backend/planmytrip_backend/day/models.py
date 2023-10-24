from django.db import models
from common.mixins import TimestampsMixin, AuthBasicInfoMixin, OrderMixin
from itinerary.models import Itinerary


class Day(TimestampsMixin, AuthBasicInfoMixin, OrderMixin):
    itinerary = models.ForeignKey(
        Itinerary, on_delete=models.CASCADE, related_name="days", null=False
    )

    def __str__(self):
        return self.name
