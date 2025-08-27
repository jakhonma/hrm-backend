from django.db import models
from .validators import phone_validator
from django.contrib.auth.hashers import make_password
from .managers import UserManager
from .utils import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    one_id = models.CharField(
        max_length=50, 
        unique=True
    )  # MTRK-000001
    phone = models.CharField(
        max_length=17,
        validators=[phone_validator],
        unique=True,
        null=True,
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f'{self.username} {self.phone}'
