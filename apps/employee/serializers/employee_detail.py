from rest_framework import serializers
from apps.employee.models import Employee
from apps.users.serializers import UserSerializer
from apps.position.serializers import PositionSerializer


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer()
    # department_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Employee._meta.get_field('department').remote_field.model.objects.all(),
    #     source='department',
    #     allow_null=True,
    #     required=False
    # )
    position = PositionSerializer()
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
