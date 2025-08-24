from rest_framework import serializers


class DepartmentListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    descreption = serializers.CharField(
        max_length=600,
        allow_blank=True
    )
    is_active = serializers.BooleanField()
    max_employee = serializers.IntegerField()
    employee_count = serializers.IntegerField(read_only=True)
    free_slots = serializers.IntegerField(read_only=True)
