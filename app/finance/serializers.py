from rest_framework import serializers
from .models import Transaction, Category, Goal, Goal_Transaction


# Транзакции
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
            # 'owner',
            'name',
            'amount',
            'date',
            'time',
            'description',
            'category',
        ]


# Категории
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            # 'owner',
            'name',
        ]


# Цели
class GoalTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal_Transaction
        fields = (
            'id',
            'goal',
            'amount',
            'date',
            'description',
        )
        read_only_fields = ('goal',)


class GoalSerializer(serializers.ModelSerializer):
    amount_now = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True, source='get_amount_now')

    class Meta:
        model = Goal
        fields = (
            'id',
            # 'owner',
            'name',
            'opening_date',
            'achievement_date',
            'amount_target',
            'amount_now',
        )
