from rest_framework import serializers


class TimestampsMixinSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        fields = "__all__"
