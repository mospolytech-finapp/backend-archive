from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Transaction
from .serializers import TransactionSerializer


class TransactionManagerViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user_id=self.request.user)

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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
