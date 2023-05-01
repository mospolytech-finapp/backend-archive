import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class LowerCaseValidator:
    def validate(self, password, user=None):
        if not re.search(r"[a-z]", password):
            raise ValidationError(
                _("This password doesn't contain any lowercase characters."),
                code="password_without_lowercase",
            )

    def get_help_text(self):
        return _("Your password must contain lowercase characters.")


class UpperCaseValidator:
    def validate(self, password, user=None):
        if not re.search(r"[A-Z]", password):
            raise ValidationError(
                _("This password doesn't contain any highercase characters."),
                code="password_without_highercase",
            )

    def get_help_text(self):
        return _("Your password must contain highercase characters.")


class NumericValidator:
    def validate(self, password, user=None):
        if not re.search(r"[0-9]", password):
            raise ValidationError(
                _("This password doesn't contain any numeric characters."),
                code="password_without_numeric",
            )

    def get_help_text(self):
        return _("Your password must contain numeric symbols.")


class SpecialCharValidator:
    def validate(self, password, user=None):
        if not re.search(
            r"[\?\!\@\#\$\%\^\&\*\(\)\_\+\{\}\[\]\<\>\/\\\|\;\:\'\"\-\+\=]",
            password
        ):
            raise ValidationError(
                _("This password doesn't contain any special characters."),
                code="password_without_special",
            )

    def get_help_text(self):
        return _("Your password must contain special symbols.")

