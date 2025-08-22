from orm import BaseRepository
from apps.department.models import Department


class DepartmentRepository(BaseRepository):
    model = Department
