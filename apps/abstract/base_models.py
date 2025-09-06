from django.db import models


class BaseAbsract(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(
        max_length=600,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
