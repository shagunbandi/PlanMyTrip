from rest_framework import serializers
from .models import Experience, ExperienceTypes
from rest_framework import serializers
from rest_enumfield import EnumField


class ExperienceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=60, allow_blank=False, trim_whitespace=True)
    description = serializers.CharField(
        max_length=180, trim_whitespace=True, required=False
    )
    google_place_id = serializers.CharField(
        max_length=120, trim_whitespace=True, required=False
    )
    type = EnumField(choices=ExperienceTypes, to_choice=lambda x: x.value)
    ticket_link = serializers.CharField(
        max_length=180, trim_whitespace=True, required=False
    )
    reservation_link = serializers.CharField(
        max_length=180, trim_whitespace=True, required=False
    )
    activity_start_time = serializers.DateTimeField(required=False)
    activity_end_time = serializers.DateTimeField(required=False)

    class Meta:
        model = Experience
        fields = "__all__"
