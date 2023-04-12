from rest_framework import serializers
from .models import Finapp_User


class FinappUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finapp_User
        fields = [
            'email',
            'password'
            'last_name',
            'first_name',
            'middle_name',
            'date_of_birth',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Finapp_User.objects.create_user(**validated_data)
        return user
