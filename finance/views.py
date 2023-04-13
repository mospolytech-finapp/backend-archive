from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Transactions
from .serializers import TransactionSerializer


class TransactionsManagerView(generics.ListCreateAPIView):
    """
    GET - возвращает транзакции, отфильтрованные по параметрам запроса
    POST - создаёт новую транзакцию
    PUT
    DELETE
    """
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Transactions.objects.filter(user_id=self.request.user.id)

        category = self.request.query_params.get('category', None)
        date = self.request.query_params.get('date', None)
        name = self.request.query_params.get('name', None)
        is_arrival = self.request.query_params.get('is_arrival', None)
        amount_min = self.request.query_params.get('amount_min', None)
        amount_max = self.request.query_params.get('amount_max', None)
        time = self.request.query_params.get('time', None)

        if category is not None:
            queryset = queryset.filter(category=category)
        if date is not None:
            queryset = queryset.filter(date=date)
        if name is not None:
            queryset = queryset.filter(name=name)
        if is_arrival is not None:
            queryset = queryset.filter(is_arrival=is_arrival)
        if amount_min is not None:
            queryset = queryset.filter(amount__gte=amount_min)
        if amount_max is not None:
            queryset = queryset.filter(amount__lte=amount_max)
        if time is not None:
            queryset = queryset.filter(time=time)

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(user_id=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            return Response(
                {'error': f'Ошибка создания транзакции: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )


