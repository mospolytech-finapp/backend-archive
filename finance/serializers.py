from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id',
            'name',
            # 'user_id',
            'amount',
            'date',
            'time',
            'description',
            'category',
        ]
        read_only_fields = ('id', 'user_id')

    def create(self, validated_data, **kwargs):
        transaction = Transaction.objects.create(**validated_data, **kwargs)
        return transaction
