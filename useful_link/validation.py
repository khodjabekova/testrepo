import os
from django.core.exceptions import ValidationError


def file_validation_exception(value):
    ext = os.path.splitext(value.name)[-1]
    valid_exceptions = ['.jpg', '.jpeg', '.png', '.svg']
    if not ext.lower() in valid_exceptions:
        raise ValidationError('Unsupported file extension.')
