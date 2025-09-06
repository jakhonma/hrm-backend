from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    avatar = serializers.ImageField(allow_null=True)


class ProfileUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    avatar = serializers.ImageField(allow_null=True)
