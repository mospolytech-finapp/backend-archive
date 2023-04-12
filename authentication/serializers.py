from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


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

    def validate_password(self, value):
        validate_password(value)  # Django password validation
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
