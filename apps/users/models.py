from django.db import models
from .validators import phone_validator, username_validator
from django.contrib.auth.hashers import make_password
from .managers import UserManager
from .utils import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
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
    date_joined = models.DateTimeField(
        _("date joined"), 
        default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username
