from rest_framework import serializers


class OrderMixinSerializer(serializers.Serializer):
    """
    A serializer for models with ordering functionality.

    This serializer provides a field for serializing the order of instances.

    Fields:
        order (int): The order of the instance.

    Note:
        The 'order' field is allowed to be null and not required, allowing for flexibility in serialization.
    """

    order = serializers.IntegerField(allow_null=True, required=False)
