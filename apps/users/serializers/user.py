from rest_framework import serializers
from apps.rbac.models import Role
from .profile import ProfileSerializer


class UserSerializer(serializers.Serializer):
    one_id = serializers.CharField(read_only=True)
    phone = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    username = serializers.CharField(required=True, max_length=150)
    role = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        required=False,
        allow_null=True
    )
    profile = ProfileSerializer()
