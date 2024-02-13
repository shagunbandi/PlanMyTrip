from common.serializers import CreateMixinSerializer
from day.serializers import DaySerializer
from rest_framework import serializers

from .models import Itinerary


class ItinerarySerializer(CreateMixinSerializer):
    days = DaySerializer(many=True, read_only=True)

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = Itinerary
        fields = "__all__"
