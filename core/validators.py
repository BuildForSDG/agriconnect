"""
The validators, both model based and API based.
"""
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class PhoneNumberValidator(validators.RegexValidator):
    regex = r'^[+]{0,1}[0-9]{9,13}'
    message = _(
        'Enter a valid phone number. This value may contain only '
        'numbers and/or + characters. Between 9 to 13 characters long.'
    )
    flags = 0
