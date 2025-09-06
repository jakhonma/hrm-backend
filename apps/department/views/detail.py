from rest_framework import generics, exceptions
from .base import BaseDepartmetCreateUpdate, BaseDepartment, BaseDepartmentList
from django.db.models import Count, F, IntegerField, ExpressionWrapper
from apps.department.models import Department


class DepartmentRetrieveAPIView(BaseDepartmentList, generics.RetrieveAPIView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        print(pk)
        try:
            department = (
                Department.objects
                .annotate(
                    employee_count=Count("employees"),
                    free_slots=ExpressionWrapper(
                        F("max_employee") - Count("employees"),
                        output_field=IntegerField()
                    )
                )
                .get(pk=pk)
            )
        except Department.DoesNotExist:
            raise exceptions.ValidationError({'msg': "Bo'lim topilmadi", 'status': 400})
        return department


class DepartmentUpdateAPIView(BaseDepartmetCreateUpdate, generics.UpdateAPIView):
    
    def get_queryset(self):
        return self.services.list()

    def perform_update(self, serializer):
        pk = self.kwargs.get('pk')
        return self.services.update(
            pk=pk,
            validated_data=serializer.validated_data
        )


class DeparmentDeleteAPIView(BaseDepartment, generics.DestroyAPIView):

    def get_object(self):
        pk = self.kwargs.get('pk')
        return self.services.get(pk=pk)
