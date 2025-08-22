from django.db import models
from .permission import Permission


class Role(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True
    )
    permissions = models.ManyToManyField(
        Permission, 
        related_name="roles", 
        blank=True
    )

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.name