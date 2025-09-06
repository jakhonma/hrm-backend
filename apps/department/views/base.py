from apps.department.serializers import DepartmentListSerializer, DepartmentSerializer
from apps.department.services import DepartmentService

class BaseDepartment:
    services = DepartmentService()


class BaseDepartmentList(BaseDepartment):
    serializer_class = DepartmentListSerializer


class BaseDepartmetCreateUpdate(BaseDepartment):
    serializer_class = DepartmentSerializer