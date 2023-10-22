from rest_framework import serializers
from .models import Experience, ExperienceTypes

from itinerary.models import Itinerary
from rest_framework import serializers
from rest_enumfield import EnumField


class ExperienceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=60, allow_blank=False, trim_whitespace=True)
    description = serializers.CharField(
        max_length=180, allow_blank=False, trim_whitespace=True
    )
    google_place_id = serializers.CharField(
        max_length=120, trim_whitespace=True, allow_null=True, required=False
    )
    type = EnumField(choices=ExperienceTypes, to_choice=lambda x: x.value)
    # ticket_link = serializers.CharField(
    #     max_length=180, trim_whitespace=True, allow_null=True, required=False
    # )
    # reservation_link = serializers.CharField(
    #     max_length=180, trim_whitespace=True, allow_null=True, required=False
    # )
    # activity_start_time = serializers.DateTimeField(allow_null=True, required=False)
    # activity_end_time = serializers.DateTimeField(allow_null=True, required=False)
    # order = serializers.IntegerField(allow_null=False, required=True)
    itinerary = serializers.IntegerField(
        allow_null=False, required=True, write_only=True
    )

    def validate_itinerary(self, value):
        try:
            itinerary_instance = Itinerary.objects.get(id=value)
        except itinerary_instance.DoesNotExist:
            raise ValueError("Itinerary with given value does not exist")
        return itinerary_instance

    class Meta:
        model = Experience
        fields = "__all__"
