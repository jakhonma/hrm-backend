from apps.employee.repository import EmployeeRepository
from orm import BaseService


class EmployeeService(BaseService):
    repository = EmployeeRepository
