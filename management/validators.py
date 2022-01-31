from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_semester(value):
    if  len(str(value)) != 5:
        raise ValidationError(_('%(value)s is not valid semester value'),params={'value': value})
    elif int(str(value)[-1]) not in [1, 2, 3]:
        raise ValidationError(_('%(value)s is not valid semester value'),params={'value': value})