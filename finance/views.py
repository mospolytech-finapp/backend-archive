from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Transactions
from .serializers import TransactionSerializer, TransactionUpdateDeleteSerializer


class TransactionsList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransactionSerializer

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


class TransactionsCreate(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

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


class TransactionsUpdate(generics.UpdateAPIView):
    serializer_class = TransactionUpdateDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        id = request.data.get('id')
        serializer = TransactionUpdateDeleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction = Transactions.objects.filter(id=id, user_id=request.user.id)
        if not transaction:
            return Response(
                {'error': 'Транзакция не найдена.'},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            serializer.update(transaction, serializer.data)
            return Response(
                {'Transaction': serializer.data},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {'error': f'Что-то пошло не так: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TransactionsDelete(generics.DestroyAPIView):
    serializer_class = TransactionUpdateDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id')
        serializer = TransactionUpdateDeleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction = Transactions.objects.filter(id=id, user_id=request.user.id)

        if not transaction:
            return Response(
                {'error': 'Транзакция не найдена.'},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            serializer.delete(transaction)
            return Response(
                {'success': 'Транзакция успешно удалена.'},
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            return Response(
                {'error': f'Что-то пошло не так: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class BaseManageView(APIView):
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'VIEWS_BY_METHOD'):
            raise Exception('VIEWS_BY_METHOD static dictionary variable must be defined on a ManageView class!')
        if request.method in self.VIEWS_BY_METHOD:
            return self.VIEWS_BY_METHOD[request.method]()(request, *args, **kwargs)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class TransactionsManageView(BaseManageView):
    VIEWS_BY_METHOD = {
        'DELETE': TransactionsDelete.as_view,
        'GET': TransactionsList.as_view,
        'PUT': TransactionsUpdate.as_view,
        'POST': TransactionsCreate.as_view
    }
