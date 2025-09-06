from rest_framework import generics, pagination
from .base import BaseDepartmentList
from django.db.models import Count, F, ExpressionWrapper, IntegerField
from apps.department.models import Department
from apps.employee.serializers import EmployeeSerializer
from apps.employee.views.base import BaseEmaployee


class DepartmentOrganizationListAPIView(BaseDepartmentList, generics.ListAPIView):
    pagination_class =pagination.LimitOffsetPagination
    # lookup_field = "organization_id"

    def get_queryset(self):

        departments = Department.objects.annotate(
            employee_count=Count("employees"),
            free_slots=ExpressionWrapper(
                F("max_employee") - Count("employees"),
                output_field=IntegerField()
            )
        )
        return departments


class DepartmentEmployeesAPIView(BaseEmaployee, generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_id = self.kwargs.get('department_id')
        return self.services.filter(department_id=department_id)
