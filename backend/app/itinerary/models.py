from common.mixins import TimestampsMixin
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from place.models import Place


class Itinerary(TimestampsMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    name = models.CharField(max_length=120)
    start_date = models.DateField(blank=True, null=True)
    places = GenericRelation(Place)

    def __str__(self):
        return self.name
