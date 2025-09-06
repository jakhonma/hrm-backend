from rest_framework import serializers
from apps.employee.models import Employee
from django.contrib.auth import get_user_model

User = get_user_model()


class EmployeeCreateUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(
        allow_null=True,
        required=False
    )
    department_id = serializers.IntegerField(
        allow_null=True,
        required=False
    )
    position_id = serializers.IntegerField(
        allow_null=True,
        required=False
    )
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    middle_name = serializers.CharField(
        max_length=255,
        allow_blank=True,
        required=False
    )
    passport_number = serializers.CharField(max_length=9)
    jshshir = serializers.CharField(max_length=14)
    birth_date = serializers.DateField(required=False, allow_null=True)
    email = serializers.EmailField(required=False, allow_null=True)
    status = serializers.ChoiceField(choices=Employee._meta.get_field('status').choices)
    is_head = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
