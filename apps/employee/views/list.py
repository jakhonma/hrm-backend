from rest_framework import generics
from apps.employee.models import Employee
from .base import BaseEmployeeDepartment
from django.db.models import Q


class EmployeeDepartmentAddAPIView(BaseEmployeeDepartment, generics.ListAPIView):
    
    def get_queryset(self):
        department_id = self.kwargs.get('department_id')
        if department_id == 0:
            employees = Employee.objects.filter(
                is_head=True,
                headed_departments__isnull=True
            )
            return employees
        return Employee.objects.filter(
            Q(headed_departments__isnull=True, is_head=True) | Q(headed_departments__id=department_id)
        )
