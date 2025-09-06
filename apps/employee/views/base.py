from apps.employee.serializers import EmployeeDepartmentListSerializer, EmployeeCreateUpdateSerializer, EmployeeSerializer
from apps.employee.services import EmployeeService


class BaseEmaployee:
    services = EmployeeService()


class BaseEmployeeCreateUpdate(BaseEmaployee):
    serializer_class = EmployeeCreateUpdateSerializer



class BaseEmployeeDepartment(BaseEmaployee):
    serializer_class = EmployeeDepartmentListSerializer
