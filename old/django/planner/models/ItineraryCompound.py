from typing import Iterable, Optional
from django.db import models
from planner.models import ItineraryElement


class ItineraryCompound(models.Model):
    """
    Itinerary compound
    """

    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name

    @property
    def elements(self):
        return ItineraryElement.objects.filter(compound__id=self.id)
