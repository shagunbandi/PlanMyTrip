from rest_framework import serializers
from .models import Itinerary
from common.serializers import AuthBasicInfoMixinSerializer, CreateMixinSerializer
from rest_framework import serializers
from day.serializers import DaySerializer


class ItinerarySerializer(AuthBasicInfoMixinSerializer, CreateMixinSerializer):
    scratchpad = serializers.CharField(allow_blank=True, allow_null=True)
    days = DaySerializer(many=True, read_only=True)

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = Itinerary
        fields = "__all__"
