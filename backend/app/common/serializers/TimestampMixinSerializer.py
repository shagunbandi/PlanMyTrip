from rest_framework import serializers


class TimestampsMixinSerializer(serializers.Serializer):
    """
    A serializer for models with timestamp fields.

    This serializer provides fields for serializing timestamp information of model instances.

    Fields:
        timestamp (datetime): The datetime when the instance was created.
        updated (datetime): The datetime when the instance was last updated.

    Note:
        Both fields are marked as read-only, indicating that they are only used for serialization and cannot be modified.
    """

    timestamp = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
