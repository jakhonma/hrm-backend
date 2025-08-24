from apps.department.serializers import DepartmentListSerializer, DepartmentSerializer
from apps.department.services import DepartmentService


class BaseDepartment:
    serializer_class = DepartmentListSerializer
    services = DepartmentService()


class BaseDepartmetCreate:
    serializer_class = DepartmentSerializer
    services = DepartmentService()