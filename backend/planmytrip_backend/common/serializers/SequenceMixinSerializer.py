from rest_framework import serializers


class SequenceMixinSerializer(serializers.Serializer):
    sequence_number = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        fields = ("sequence_number",)
