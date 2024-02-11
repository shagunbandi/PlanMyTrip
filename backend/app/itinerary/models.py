from common.mixins import AuthBasicInfoMixin, TimestampsMixin
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Itinerary(TimestampsMixin, AuthBasicInfoMixin):
    start_date = models.DateField(blank=True, null=True)

    @property
    def places(self):
        from place.models import Place  # Import moved inside method

        return Place.objects.filter(
            parent_type=ContentType.objects.get_for_model(self), parent_id=self.id
        )

    def __str__(self):
        return self.name
