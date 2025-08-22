from django.db import models
from django.utils import timezone


class Organization(models.Model):
    name = models.CharField(max_length=255)
    one_id = models.CharField(
        max_length=50, 
        unique=True
    )  # 000001
    phone = models.CharField(
        max_length=17, 
        null=True,
        blank=True
    )
    balance = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0.00
    )
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    # def employee_count(self):
    #     return self.employees.count()

    class Meta:
        db_table = 'organization'

    def __str__(self):
        return self.name
