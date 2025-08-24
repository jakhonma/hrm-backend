from django.db import models
from apps.abstract.base_models import BaseAbsract


class Department(BaseAbsract):
    head = models.OneToOneField(
        to='employee.Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headed_departments'
    )
    max_employee = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'department'
