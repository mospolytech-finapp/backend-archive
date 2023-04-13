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
    def create(self, validated_data,**kwargs):
        transaction = Transactions.objects.create(**validated_data,**kwargs)
        return transaction