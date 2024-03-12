from common.models import OwnerModel, TimestampModel
from django.db import models
from itinerary.models.itinerary import Itinerary
from ordered_model.models import OrderedModel


class Roster(OwnerModel, OrderedModel, TimestampModel):
    title = models.CharField(max_length=120, null=True, blank=True)
    itinerary = models.ForeignKey(
        Itinerary,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="rosters",
    )

    order_with_respect_to = "itinerary"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.itinerary.owner != self.owner:
                raise ValueError(
                    "You are not allowed to create a roster in this itinerary."
                )
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("order",)
