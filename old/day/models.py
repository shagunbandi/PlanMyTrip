from common.mixins import TimestampsMixin
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from itinerary.models import Itinerary
from ordered_model.models import OrderedModel
from place.models import Place


class Day(TimestampsMixin, OrderedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    name = models.CharField(max_length=120)
    itinerary = models.ForeignKey(
        Itinerary, on_delete=models.CASCADE, related_name="days", null=False
    )
    places = GenericRelation(Place)

    order_with_respect_to = "itinerary"

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)
