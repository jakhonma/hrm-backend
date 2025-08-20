from django.db import models


class Permission(models.Model):
    code = models.CharField(max_length=100, unique=True)  # masalan: "view_employee"
    name = models.CharField(max_length=255)  # masalan: "Can View Employee"

    def __str__(self):
        return self.name
