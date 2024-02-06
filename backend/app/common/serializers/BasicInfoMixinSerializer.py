from django.contrib.auth.models import User  # Import User model if not already imported
from rest_framework import serializers


class AuthBasicInfoMixinSerializer(serializers.Serializer):
    """
    A serializer for models containing basic authentication-related information.

    This serializer provides fields for serializing basic information related to authentication,
    such as the name of the entity and the user associated with it.

    Fields:
        name (str): The name of the entity.
        user (int): The ID of the user associated with the entity.

    Note:
        This serializer is intended to be used with models that include the AuthBasicInfoMixin.
    """

    name = serializers.CharField(max_length=60)
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, write_only=True
    )
