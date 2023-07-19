from django.db.models import fields
from rest_framework import serializers
# from .models import Item
 
# class PlacesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = ('category', 'subcategory', 'name', 'amount')


class DistanceBetweenPlacesRequestSerializer(serializers.Serializer):
    origin_place_id = serializers.CharField(min_length=1)
    destination_place_id = serializers.CharField(min_length=1)
    # mode = serializers.CharField(min_length=0)

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)


class DistanceBetweenPlacesResponseSerializer(serializers.Serializer):
    origin_address=serializers.CharField(min_length=1)
    destination_address=serializers.CharField(min_length=1)
    distance_in_meters=serializers.IntegerField()
    duration_in_mins=serializers.IntegerField()

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)

