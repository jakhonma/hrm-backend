from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    # def employee_count(self):
    #     return self.employees.count()

    def __str__(self):
        return self.name
