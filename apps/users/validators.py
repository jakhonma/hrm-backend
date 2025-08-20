from django.core.exceptions import ValidationError
import re
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()


def phone_validator(value):
    if not re.match(r'^\+998\d{2}\s?\d{3}\s?\d{2}\s?\d{2}$', value):
        raise ValidationError("Telefon raqami noto'g'ri formatda! (Masalan: +998 90 123 45 67)")
