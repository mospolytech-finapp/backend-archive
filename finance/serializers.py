from rest_framework import serializers
from .models import Transaction, Category


class FilteredCategoryPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.context.get('request')
        if request:
            return queryset.filter(owner=request.user)
        return queryset


class TransactionSerializer(serializers.ModelSerializer):
    category = FilteredCategoryPrimaryKeyRelatedField(
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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            # 'owner',
            'name',
        ]
