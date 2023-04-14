from rest_framework import serializers
from .models import Transactions


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = [
            'id',
            'name',
            # 'user_id',
            'amount',
            'is_arrival',
            'date',
            'time',
            'description',
            'category',
        ]
        read_only_fields = ('id', 'user_id')

    def create(self, validated_data, **kwargs):
        transaction = Transactions.objects.create(**validated_data, **kwargs)
        return transaction


class TransactionUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = [
            'id',
            'name',
            # 'user_id',
            'amount',
            'is_arrival',
            'date',
            'time',
            'description',
            'category',
        ]
        extra_kwargs = {
            'category': {'required': False},
            'amount': {'required': False},
            'is_arrival': {'required': False},
        }
        read_only_fields = ('id', 'user_id')

    def update(self, instance, validated_data):
        instance.update(**validated_data)
        return instance

    def delete(self, instance):
        instance.delete()
        return instance
