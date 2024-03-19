from common.models import OwnerModel, TimestampModel
from django.db import models
from itinerary.models.itinerary import Itinerary
from ordered_model.models import OrderedModel


class Agenda(OwnerModel, OrderedModel, TimestampModel):
    title = models.CharField(max_length=120, null=True, blank=True)
    itinerary = models.ForeignKey(
        Itinerary,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="agendas",
    )

    order_with_respect_to = "itinerary"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("order",)
