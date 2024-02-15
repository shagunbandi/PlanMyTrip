from common.models import GenericRelationOrderModel, OwnerModel, TimestampModel
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from ordered_model.models import OrderedModel


class Places(OwnerModel, GenericRelationOrderModel, TimestampModel):
    title = models.CharField(max_length=120)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    parent = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("order",)


class Itinerary(OwnerModel, TimestampModel):
    title = models.CharField(max_length=120)
    places = GenericRelation(Places)

    def __str__(self):
        return self.title


class Day(OwnerModel, OrderedModel, TimestampModel):
    title = models.CharField(max_length=120)
    itinerary = models.ForeignKey(
        Itinerary,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="days",
    )
    places = GenericRelation(Places)

    order_with_respect_to = "itinerary"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("order",)
