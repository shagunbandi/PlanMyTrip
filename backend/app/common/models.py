from django.contrib.auth.models import User
from django.db import models


class OwnerModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)

    class Meta:
        abstract = True
