from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import (
    Transaction,
    Category,
    Goal,
    Goal_Transaction,
)
from .serializers import (
    TransactionSerializer,
    CategorySerializer,
    GoalSerializer,
    GoalTransactionSerializer,
)


# Транзацкии
class TransactionManagerViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)

    def filter_queryset(self, queryset):
        filter_params = self.request.query_params.dict()

        if 'amount_min' in filter_params:
            queryset = queryset.filter(amount__gte=filter_params['amount_min'])
            del filter_params['amount_min']

        if 'amount_max' in filter_params:
            queryset = queryset.filter(amount__lte=filter_params['amount_max'])
            del filter_params['amount_max']

        queryset = queryset.filter(**filter_params)

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data.copy())
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


# Категории
class CategoryManagerViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data.copy())
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


# Цели
class GoalManagerViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data.copy())
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


# Транзакции целей
class GoalTransactionManagerViewSet(viewsets.ModelViewSet):
    serializer_class = GoalTransactionSerializer
    queryset = Goal_Transaction.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        goal_id = self.kwargs['goal_id']
        return self.queryset.filter(goal__id=goal_id, goal__owner=self.request.user)

    def create(self, request, *args, **kwargs):
        goal_id = self.kwargs['goal_id']
        try:
            goal = Goal.objects.get(id=goal_id, owner=request.user)
        except Goal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data.copy())
        serializer.is_valid(raise_exception=True)
        serializer.save(goal=goal)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
