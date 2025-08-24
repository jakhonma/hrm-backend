from rest_framework import generics
from .base import BaseOrganization


class OrganizationListAPIView(BaseOrganization, generics.ListAPIView):
    def get_queryset(self):
        return self.services.list()
