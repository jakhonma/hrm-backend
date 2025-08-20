from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User


@receiver(post_save, sender=User)
def generate_one_id(sender, instance, created, **kwargs):
    if created and not instance.one_id:
        instance.one_id = f"{instance.id:06d}"
        instance.save(update_fields=['one_id'])
