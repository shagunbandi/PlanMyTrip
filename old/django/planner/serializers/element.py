from rest_framework import serializers
from planner.models import ItineraryElement


class ItineraryElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryElement
        fields = (
            "id",
            "compound",
            "place_id",
            "name",
            "city",
            "category",
            "activity_time_in_mins",
            "rating_value",
            "rating_count",
            "duration_in_mins",
            "distance_in_meters",
            "latitude",
            "longitude",
            "nth_day",
            "activity_number",
        )

    def is_valid(self, *, raise_exception=True):
        return super().is_valid(raise_exception=raise_exception)
