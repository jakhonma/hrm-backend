from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import User


class UsernameOrPhoneBackend(ModelBackend):
    """
    Username yoki phone_number orqali login qilish uchun backend
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(phone=username))
        except User.DoesNotExist:
            return None

        if user and user.check_password(password):
            return user
        return None
