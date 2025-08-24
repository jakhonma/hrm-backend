from rest_framework import serializers


class EmployeeDepartmentListSerializer(serializers.Serializer):
    """
    Department qo'shish uchun serializer
    """
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
