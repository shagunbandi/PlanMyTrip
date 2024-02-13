from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Places(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    title = models.CharField(max_length=120)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    parent = GenericForeignKey("content_type", "object_id")


class Itinerary(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=120)
    places = GenericRelation(Places)


class Day(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    itinerary = models.ForeignKey(
        Itinerary,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="days",
    )
    title = models.CharField(max_length=120)
    places = GenericRelation(Places)
