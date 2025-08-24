from rest_framework import generics
from .base import BaseEmployeeDepartment


class EmployeeDepartmentAddAPIView(BaseEmployeeDepartment, generics.ListAPIView):
    def get_queryset(self):
        return self.services.filter(headed_departments__isnull=True)
