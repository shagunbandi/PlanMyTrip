from common.mixins import AuthBasicInfoMixin, TimestampsMixin
from django.db import models


class Itinerary(TimestampsMixin, AuthBasicInfoMixin):
    start_date = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.name
