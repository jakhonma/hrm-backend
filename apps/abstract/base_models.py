from django.db import models


class BaseAbsract(models.Model):
    name = models.CharField(max_length=200)
    descreption = models.CharField(max_length=600)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
