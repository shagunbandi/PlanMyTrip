from django.db import models
from common.mixins import TimestampsMixin, AuthBasicInfoMixin


class Itinerary(TimestampsMixin, AuthBasicInfoMixin):
    scratchpad = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
