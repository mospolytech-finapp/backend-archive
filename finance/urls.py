from django.urls import path
from .views import *

urlpatterns = [
    path('transactions/', TransactionsManageView.as_view(), name='transactions-manager'),
]
