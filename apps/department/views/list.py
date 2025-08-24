from rest_framework import generics, pagination
from .base import BaseDepartment
from django.db.models import Count, F, ExpressionWrapper, IntegerField
from apps.department.models import Department



class DepartmentOrganizationListAPIView(BaseDepartment, generics.ListAPIView):
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
