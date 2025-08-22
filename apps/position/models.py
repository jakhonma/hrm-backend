from django.db import models
from apps.abstract.base_models import BaseAbsract


class Position(BaseAbsract):
    class Meta:
        db_table = 'position'
