from django.contrib.auth import authenticate, login
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from phonenumber_field.serializerfields import PhoneNumberField


class LoginSerializer(serializers.Serializer):
    phone = PhoneNumberField()
    password = serializers.CharField()
    token_class = RefreshToken

    default_error_messages = {
        "no_active_account": _("No active account found with the given credentials")
    }

    def validate(self, attrs):
        authenticate_kwargs = {
            "phone": attrs["phone"],
            "password": attrs["password"],
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        user = authenticate(**authenticate_kwargs)

        if user is None:
            raise ValidationError("Phone yoki Password xato")

        login(authenticate_kwargs["request"], user)
        refresh = self.get_token(user)

        attrs["refresh"] = str(refresh)
        attrs["access"] = str(refresh.access_token)
        attrs['user_id'] = user.id

        del attrs["password"], attrs["phone"]

        return attrs

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)