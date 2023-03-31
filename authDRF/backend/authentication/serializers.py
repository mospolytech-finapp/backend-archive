from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'last_name', 'first_name', 'middle_name', 'email', 'date_of_birth', 'gender']
