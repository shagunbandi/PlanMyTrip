from rest_framework import serializers


class DistanceBetweenPlacesRequestSerializer(serializers.Serializer):
    origin_place_id = serializers.CharField(min_length=1)
    destination_place_id = serializers.CharField(min_length=1)
    # mode = serializers.CharField(min_length=0)

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
