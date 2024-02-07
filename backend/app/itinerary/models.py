from common.mixins import AuthBasicInfoMixin, TimestampsMixin
from django.db import models


class Itinerary(TimestampsMixin, AuthBasicInfoMixin):
    start_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
