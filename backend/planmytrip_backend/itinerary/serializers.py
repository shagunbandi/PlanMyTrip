from rest_framework import serializers
from .models import Itinerary


class ItinerarySerializer(serializers.ModelSerializer):
    def validate_timeline(self, timeline):
        if not isinstance(timeline, list):
            raise serializers.ValidationError(
                "Timeline should be a list of experience ids"
            )
        return timeline

    class Meta:
        model = Itinerary
        fields = "__all__"
