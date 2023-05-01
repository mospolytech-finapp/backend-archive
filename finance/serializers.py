from rest_framework import serializers
from .models import Transaction, Category


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id',
            'name',
            # 'owner',
            'amount',
            'date',
            'time',
            'description',
            'category',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            # 'owner',
            'name',
        ]
