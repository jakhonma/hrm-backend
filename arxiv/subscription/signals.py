from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Subscription

@receiver(pre_save, sender=Subscription)
def update_updated_at(sender, instance, **kwargs):
    instance.updated_at = timezone.now()