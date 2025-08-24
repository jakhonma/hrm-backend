from apps.employee.serializers import EmployeeDepartmentListSerializer
from apps.employee.services import EmployeeService


class BaseEmployeeDepartment:
    serializer_class = EmployeeDepartmentListSerializer
    services = EmployeeService()
