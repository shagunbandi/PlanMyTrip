from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class GenericRelationMixin(models.Model):
    parent_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    parent_id = models.PositiveIntegerField()
    parent = GenericForeignKey("parent_type", "parent_id")

    class Meta:
        abstract = True
