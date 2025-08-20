from django.db import models


class EmployeeStatus(models.TextChoices):
    ACTIVE = 'active'
    VACATION = 'vacation'
    FIRED = 'fired'
