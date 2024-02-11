from common.mixins import AuthBasicInfoMixin, TimestampsMixin
from django.contrib.contenttypes.models import ContentType
from django.db import models
from itinerary.models import Itinerary
from ordered_model.models import OrderedModel


class Day(TimestampsMixin, AuthBasicInfoMixin, OrderedModel):
    itinerary = models.ForeignKey(
        Itinerary, on_delete=models.CASCADE, related_name="days", null=False
    )

    order_with_respect_to = "itinerary"

    @property
    def places(self):
        from place.models import Place

        return Place.objects.filter(
            parent_type=ContentType.objects.get_for_model(self), parent_id=self.id
        )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)
