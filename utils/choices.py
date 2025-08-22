from django.db import models


class EmployeeStatus(models.TextChoices):
    ACTIVE = 'active'
    VACATION = 'vacation'
    FIRED = 'fired'


class SubscriptionStatus(models.TextChoices):
    ACTIVE = 'active'
    EXPIRED = 'expired'
    SUSPENDED = 'suspended'


class PaymentStatus(models.TextChoices):
    PENDING = 'pending'
    PAID = 'paid'
    FAILED = 'failed'
