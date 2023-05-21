from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def validate_text(value):
    print("Validating value % ")
    if not "task" in value:
        raise ValidationError(_("Text %(val) must contain task word") % {"val":value})
    else:
        return value