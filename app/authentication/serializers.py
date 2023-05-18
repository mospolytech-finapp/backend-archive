from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError
from datetime import date
from django.utils.translation import gettext as _

User = get_user_model()


class FinappUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'last_name',
            'first_name',
            'middle_name',
            'date_of_birth',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, password):
        validate_password(password)  # Django password validation
        return password

    def validate_date_of_birth(self, date_of_birth):
        if date_of_birth > date.today():
            raise ValidationError(
                _("Birth date cannot be in the future."),
                code="birthday_in_future",
            )
        return date_of_birth

    def create(self, validated_data):
        if hasattr(validated_data, "date_of_birth"):
            self.validate_date_of_birth(validated_data.date_of_birth)

        user = User.objects.create_user(**validated_data)
        return user
