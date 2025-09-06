from rest_framework import generics
from .base import BaseEmployeeCreateUpdate, BaseEmaployee


class EmployeeUpdateAPIView(BaseEmployeeCreateUpdate, generics.UpdateAPIView):

    def perform_update(self, serializer):
        pk = self.kwargs.get('pk')
        return self.services.update(
            pk=pk,
            validated_data=serializer.validated_data
        )


class EmployeeDeleteAPIView(BaseEmaployee, generics.DestroyAPIView):

    def get_object(self):
        pk = self.kwargs.get('pk')
        return self.services.get(pk=pk)
