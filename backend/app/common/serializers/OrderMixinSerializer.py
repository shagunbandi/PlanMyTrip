from rest_framework import serializers


class OrderMixinSerializer(serializers.Serializer):
    """
    Serializer for models with ordering functionality.

    This serializer provides a field for serializing the order of instances.

    Fields:
        order (int): The order of the instance. Read-only.

    Note:
        The 'order' field is read-only, indicating that it is only used for serialization and cannot be modified.
        It is allowed to be null and not required, allowing for flexibility in serialization.
    """

    order = serializers.IntegerField(read_only=True)
