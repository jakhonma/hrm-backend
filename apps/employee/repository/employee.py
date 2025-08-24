from orm import BaseRepository
from apps.employee.models import Employee


class EmployeeRepository(BaseRepository):
    model = Employee
