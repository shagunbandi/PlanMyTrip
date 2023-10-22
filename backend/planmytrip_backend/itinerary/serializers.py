from rest_framework import serializers
from .models import Itinerary
from common.serializers import AuthBasicInfoMixinSerializer, CreateMixinSerializer
from rest_framework import serializers


class ItinerarySerializer(AuthBasicInfoMixinSerializer, CreateMixinSerializer):
    scratchpad = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = Itinerary
        fields = ["id", "scratchpad", "name", "notes", "user"]
