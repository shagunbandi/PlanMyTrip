from rest_framework import serializers
from planner.models import ItineraryCompound
from .element import ItineraryElementSerializer


class CreateItineraryCompoundSerializer(serializers.Serializer):
    name = serializers.CharField()
    place = serializers.CharField()
    number_of_days = serializers.IntegerField()
    note = serializers.CharField()
    circular = serializers.BooleanField(default=True)
    is_mock = serializers.BooleanField(default=False)

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)


class ItineraryCompoundSerializer(serializers.ModelSerializer):
    elements = ItineraryElementSerializer(many=True)

    class Meta:
        model = ItineraryCompound
        fields = ("id", "name", "elements")
