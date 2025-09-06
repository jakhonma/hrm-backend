from .base import BaseDepartmetCreateUpdate
from rest_framework import generics


class DeparmentCreateAPIView(BaseDepartmetCreateUpdate, generics.CreateAPIView):

    def perform_create(self, serializer):
        print(serializer.validated_data)
        return self.services.create(serializer.validated_data)
