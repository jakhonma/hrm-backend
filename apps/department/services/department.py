from apps.department.repository import DepartmentRepository
from orm import BaseService


class DepartmentService(BaseService):
    repository = DepartmentRepository
