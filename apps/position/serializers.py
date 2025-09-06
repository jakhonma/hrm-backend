from rest_framework import serializers


class PositionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(
        max_length=600,
        allow_blank=True
    )
