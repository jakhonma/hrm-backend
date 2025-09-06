from rest_framework import generics
from .base import BaseUserAPIView


class UserRetrieveAPIView(BaseUserAPIView, generics.RetrieveAPIView):

    def get_object(self):
        pk = self.kwargs.get("pk")
        return self.services.get(pk=pk)
