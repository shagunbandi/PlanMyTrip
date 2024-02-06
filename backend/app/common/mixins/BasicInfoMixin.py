from django.contrib.auth.models import User
from django.db import models


class AuthBasicInfoMixin(models.Model):
    """
    A mixin for models containing basic authentication-related information.

    This mixin provides fields for storing basic information related to authentication,
    such as the name of the entity and the user associated with it.

    Attributes:
        name (str): The name of the entity.
        user (User): The user associated with the entity.
    """

    name = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True
