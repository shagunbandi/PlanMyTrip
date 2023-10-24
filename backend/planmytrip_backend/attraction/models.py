from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField
from common.mixins import TimestampsMixin, AuthBasicInfoMixin, SequenceMixin
from day.models import Day


class Category(ChoiceEnum):
    HIKING = "hiking"
    MONUMENT = "monument"
    CLASSES = "classes"
    LOCALITY = "locality"
    EXPERIENCE = "experience"
    OTHER = "other"

    def __str__(self):
        return self.value


class Attraction(TimestampsMixin, AuthBasicInfoMixin, SequenceMixin):
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, related_name="attractions", null=False
    )
    category = EnumChoiceField(Category, default=Category.OTHER)

    def __str__(self):
        return self.name
