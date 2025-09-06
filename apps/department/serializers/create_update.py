from rest_framework import serializers


class DepartmentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(
        max_length=600,
        required=False,
        allow_blank=True
    )
    head_id = serializers.IntegerField(allow_null=True)
    max_employee = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Serializer chaqirilganda frontenddan kelayotgan datani ko'rish
        if hasattr(self, 'initial_data'):
            print("Frontenddan kelgan data:", self.initial_data)