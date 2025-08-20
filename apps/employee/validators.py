from django.core.exceptions import ValidationError
import datetime

def validate_birth_date(value):
    today = datetime.date.today()
    if value > today:
        raise ValidationError("Tug‘ilgan sana kelajak bo‘lishi mumkin emas.")
    if value.year < 1900:
        raise ValidationError("Tug‘ilgan sana 1900-yildan oldin bo‘lishi mumkin emas.")
