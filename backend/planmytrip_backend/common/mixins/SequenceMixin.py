from django.db import models


class SequenceMixin(models.Model):
    sequence_number = models.IntegerField(blank=True, default=-1)

    class Meta:
        abstract = True
