from django.db import models
from django.utils import timezone


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True, 
        null=True
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    duration_months = models.IntegerField()
    max_employee_count = models.IntegerField(default=10)
    # features = models.TextField(blank=True, null=True)  # JSON uchun JSONField ishlatilishi mumkin
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'subscription_plans'

    def __str__(self):
        return self.name
