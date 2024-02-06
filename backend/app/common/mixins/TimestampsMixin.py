from django.db import models


class TimestampsMixin(models.Model):
    """
    A mixin for adding timestamp fields to models.

    This mixin provides two timestamp fields:
        - timestamp: Represents the datetime when the instance was created.
        - updated: Represents the datetime when the instance was last updated.

    Attributes:
        timestamp (datetime): The datetime when the instance was created.
        updated (datetime): The datetime when the instance was last updated.

    Note:
        By default, the 'timestamp' field is automatically set to the current datetime when the instance is created.
        The 'updated' field is automatically updated to the current datetime whenever the instance is saved.

    Meta:
        abstract (bool): Indicates that this model is abstract and not meant to be used on its own.
    """

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True
