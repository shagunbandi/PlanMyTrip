from django.db import models
from common.mixins import TimestampsMixin, AuthBasicInfoMixin
from ordered_model.models import OrderedModel
from itinerary.models import Itinerary


class Day(TimestampsMixin, AuthBasicInfoMixin, OrderedModel):
    itinerary = models.ForeignKey(
        Itinerary, on_delete=models.CASCADE, related_name="days", null=False
    )

    order_with_respect_to = "itinerary"

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)
