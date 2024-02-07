from common.serializers import (
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    TimestampsMixinSerializer,
)
from day.serializers import DaySerializer
from rest_framework import serializers

from .models import Itinerary


class ItinerarySerializer(
    TimestampsMixinSerializer, AuthBasicInfoMixinSerializer, CreateMixinSerializer
):
    days = DaySerializer(many=True, read_only=True)
    # start_date = serializers.DateField()

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = Itinerary
        fields = "__all__"
