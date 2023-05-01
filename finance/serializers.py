from rest_framework import serializers
from .models import Transaction, Category


class TransactionSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
    )

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

    def get_fields(self):
        fields = super().get_fields()

        fields['category'].queryset = fields['category'].queryset.filter(
            owner=self.context['request'].user)

        return fields


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            # 'owner',
            'name',
        ]
