from django.urls import path
from .views import TransactionsManagerView

urlpatterns = [
    path('transactions/', TransactionsManagerView.as_view(), name='transactions-manager'),
]
