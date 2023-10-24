from rest_framework import serializers


class OrderMixinSerializer(serializers.Serializer):
    order = serializers.IntegerField(allow_null=True, required=False)
