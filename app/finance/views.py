from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from django.utils.translation import gettext as _

from decimal import Decimal

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
        return Transaction.objects.all()

    def filter_queryset(self, queryset):
        filter_params = self.request.query_params.dict()

        queryset = queryset.filter(owner=self.request.user)

        amount_min = filter_params.pop('amount_min', None)
        if amount_min:
            queryset = queryset.filter(amount__gte=amount_min)

        amount_max = filter_params.pop('amount_max', None)
        if amount_max:
            queryset = queryset.filter(amount__lte=amount_max)

        date_min = filter_params.pop('date_min', None)
        if date_min:
            queryset = queryset.filter(date__gte=date_min)

        date_max = filter_params.pop('date_max', None)
        if date_max:
            queryset = queryset.filter(date__lte=date_max)

        category = filter_params.pop('category', None)
        if category:
            queryset = queryset.filter(category__id=category)

        description = filter_params.pop('description', None)
        if description:
            queryset = queryset.filter(description__icontains=description)

        name = filter_params.pop('name', None)
        if description:
            queryset = queryset.filter(name__icontains=name)

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

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='amount_min',
                type=OpenApiTypes.NUMBER,
                location=OpenApiParameter.QUERY,
                description='Minimum transaction amount',
                required=False
            ),
            OpenApiParameter(
                name='amount_max',
                type=OpenApiTypes.NUMBER,
                location=OpenApiParameter.QUERY,
                description='Maximum transaction amount',
                required=False
            ),
            OpenApiParameter(
                name='date_min',
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                description='Earliest transaction date',
                required=False
            ),
            OpenApiParameter(
                name='date_max',
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                description='Latest transaction date',
                required=False
            ),
            OpenApiParameter(
                name='category',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description='Filter by category ID',
                required=False
            ),
            OpenApiParameter(
                name='description',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Filter by transaction description',
                required=False
            ),
            OpenApiParameter(
                name='name',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Filter by transaction name',
                required=False
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


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

    def get_queryset(self):
        return Goal.objects.filter(owner=self.request.user)

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
    lookup_field = 'id'

    def get_queryset(self):
        goal_id = self.kwargs['goal_id']
        return Goal_Transaction.objects.filter(goal__id=goal_id, goal__owner=self.request.user)

    def create(self, request, *args, **kwargs):
        goal_id = self.kwargs['goal_id']
        try:
            goal = Goal.objects.get(id=goal_id, owner=request.user)
        except Goal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data.copy())
        serializer.is_valid(raise_exception=True)

        if goal.get_amount_now() + Decimal(serializer.validated_data['amount']) < 0:
            return Response(
                {
                    "type": "validation_error",
                    "errors": [{
                        "code": "invalid",
                        "detail": _("The sum of all goal transactions cannot be less than zero."),
                        "attr": "amount"
                    }]
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save(goal=goal)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
