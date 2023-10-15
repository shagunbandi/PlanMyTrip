from rest_framework import serializers
from rest_framework.fields import empty


class DistanceBetweenPlacesRequestSerializer(serializers.Serializer):
    origin_place_id = serializers.CharField(required=True)
    destination_place_id = serializers.CharField(required=True)
    mode = serializers.CharField(required=False)

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.is_valid()
