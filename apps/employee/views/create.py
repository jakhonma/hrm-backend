from rest_framework import generics
from .base import BaseEmployeeCreateUpdate


class EmployeeCreateAPIView(BaseEmployeeCreateUpdate, generics.CreateAPIView):

    def perform_create(self, serializer):
        return self.services.create(validated_data=serializer.validated_data)
