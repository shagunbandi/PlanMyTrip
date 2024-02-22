from common.enums import RESERVATION_STATUS
from common.models import GenericRelationOrderModel, OwnerModel, TimestampModel
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from django.db import models
from enumchoicefield import EnumChoiceField
from ordered_model.models import OrderedModel


class Place(OwnerModel, GenericRelationOrderModel, TimestampModel):
    title = models.CharField(max_length=120)
    text = models.TextField(blank=True, null=True, default="")
    link = models.CharField(max_length=120, null=True, blank=True)
    file = models.FileField(upload_to="reservations/", null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    status = EnumChoiceField(RESERVATION_STATUS, default=RESERVATION_STATUS.UNSET)
    cost = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=3, null=True, blank=True, default="EUR")

    # Generic Relation with Parent
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    parent = GenericForeignKey("content_type", "object_id")

    def save(self, *args, **kwargs):
        if self.file.name:
            filename = f"{self.id}_{self.file.name}"
            self.file.name = (
                f"{self.user.id}/{self.content_type.model}/place/{filename}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("order",)


class Itinerary(OwnerModel, TimestampModel):
    title = models.CharField(max_length=120)
    places = GenericRelation(Place)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

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
    places = GenericRelation(Place)

    order_with_respect_to = "itinerary"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("order",)
