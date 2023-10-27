from django.db import models
from django.contrib.auth.models import User


class BasicInfoMixin(models.Model):
    name = models.CharField(max_length=60)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class AuthBasicInfoMixin(BasicInfoMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True
