from common.models import OwnerModel, TimestampModel
from django.db import models


class Itinerary(OwnerModel, TimestampModel):
    title = models.CharField(max_length=120)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
