from django.db import models
from apps.users.models import User
from django.core.validators import RegexValidator
from .validators import validate_birth_date
from utils.choices import EmployeeStatus
from django.conf import settings


class Employee(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='employees'
    )
    department = models.ForeignKey(
        to='department.Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees'
    )
    position = models.ForeignKey(
        to='position.Position',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    passport_number = models.CharField(
        max_length=9,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{2}\d{7}$',
                message="Passport number must be in format: 2 uppercase letters + 7 digits (e.g. AB1234567)."
            )
        ]
    )
    jshshir = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex=r'^\d{14}$',
                message="JShShIR must be exactly 14 digits."
            )
        ],
        unique=True
    )
    birth_date = models.DateField(
        validators=[validate_birth_date],
        null=True,
        blank=True
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=10,
        choices=EmployeeStatus.choices,
        default=EmployeeStatus.ACTIVE
    )
    is_head = models.BooleanField(default=False)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
