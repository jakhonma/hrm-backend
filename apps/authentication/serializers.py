from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import gettext_lazy as _
from apps.users.backends import MultiFieldAuthBackend

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "username"  # default; agar email bo‘lsa o‘zgartiring
    auth = MultiFieldAuthBackend()

    def validate(self, attrs):
        username = attrs.get(self.username_field)
        password = attrs.get("password")

        if not username or not password:
            raise AuthenticationFailed(_("Username and password are required."))

        # user = authenticate(
        #     request=self.context.get("request"),
        #     username=username,
        #     password=password,
        # )
        user = self.auth.authenticate(
            request=self.context.get("request"),
            username=username,
            password=password,
        )
        if not user:
            raise AuthenticationFailed(_("Invalid credentials."))

        if not user.is_active:
            raise AuthenticationFailed(_("User is inactive."))

        # oddiy TokenObtainPairSerializer validate() chaqirib, access/refresh yasaymiz
        data = super().validate(attrs)

        # Qo‘shimcha claimlar (token ichida ko‘rinasiz)
        data["user"] = {
            "id": self.user.id,
            "username": self.user.username,
            "is_staff": self.user.is_staff,
            "is_superuser": self.user.is_superuser,
        }
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # token claimlarini kengaytirish
        token["username"] = user.username
        token["is_staff"] = user.is_staff
        token["roles"] = getattr(user, "roles", []) if hasattr(user, "roles") else []
        return token
