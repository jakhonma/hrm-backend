from django.db import models
from apps.organization.models import Organization
from apps.abstract.base_models import BaseAbsract


class Department(BaseAbsract):
    organization = models.ForeignKey(
        to=Organization,
        on_delete=models.CASCADE,
        related_name="departments"
    )
