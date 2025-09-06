from django.db import models
from .user import User
from utils.directory import directory_path


class Profile(models.Model):
    user = models.OneToOneField(
        to=User, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    avatar = models.ImageField(
        upload_to=directory_path,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user}"