from django.db import models
from django.utils import timezone
from apps.organization.models import Organization
from apps.subscription_plan.models import SubscriptionPlan
from utils.choices import SubscriptionStatus, PaymentStatus


class Subscription(models.Model):
    organization = models.ForeignKey(
        to=Organization, 
        on_delete=models.CASCADE, 
        related_name='subscriptions'
    )
    plan = models.ForeignKey(
        SubscriptionPlan, 
        on_delete=models.CASCADE, 
        related_name='subscriptions'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20, 
        choices=SubscriptionStatus.choices, 
        default=SubscriptionStatus.ACTIVE
    )
    payment_status = models.CharField(
        max_length=20, 
        choices=PaymentStatus.choices, 
        default=PaymentStatus.PENDING
    )
    overpaid_amount = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0.00
    )
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'subscriptions'

    def __str__(self):
        return f"{self.organization.name} - {self.plan.name} ({self.status})"
