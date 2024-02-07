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
    """
    Serializer for the Itinerary model.
    """

    days = DaySerializer(many=True, read_only=True)

    def create(self, validated_data):
        """
        Create a new itinerary instance.

        Args:
            validated_data (dict): The validated data to create the itinerary.

        Returns:
            obj: The newly created itinerary object.
        """
        return super().create(validated_data)

    class Meta:
        model = Itinerary
        fields = "__all__"
