from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_score(value):
    if value > 10 or value < 0:
        raise ValidationError(_('%(value)s is not valid score'),params={'value': value})