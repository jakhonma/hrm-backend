from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.rbac.models import Role
from django.contrib.auth.models import _user_has_module_perms


class PermissionsMixin(models.Model):
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )

    class Meta:
        abstract = True
    
    def has_permission(self, permission_code: str) -> bool:
        """Userda permission bor yoki yo'qligini tekshiradi"""
        if self.role:
            return self.role.permissions.filter(code=permission_code).exists()
        return False
    
    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True
    
    def has_module_perms(self, app_label):
        """
        Return True if the user has any permissions in the given app label.
        Use similar logic as has_perm(), above.
        """
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        return _user_has_module_perms(self, app_label)
