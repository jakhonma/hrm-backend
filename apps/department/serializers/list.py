from rest_framework import serializers


class DepartmentListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    descreption = serializers.CharField(
        max_length=600,
        allow_blank=True
    )
    employee_count = serializers.SerializerMethodField()

    def get_employee_count(self, obj):
        return obj.employees.count()
