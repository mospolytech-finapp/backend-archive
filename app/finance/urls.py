from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TransactionManagerViewSet,
    CategoryManagerViewSet,
    GoalManagerViewSet,
    GoalTransactionManagerViewSet,
)

router = DefaultRouter()
router.register(r'transactions', TransactionManagerViewSet, 'transaction')
router.register(r'categories', CategoryManagerViewSet, 'category')
router.register(r'goals', GoalManagerViewSet, 'goal')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'goals/<int:goal_id>/transactions/',
        GoalTransactionManagerViewSet.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='goal_transaction'
    ),
    path(
        'goals/<int:goal_id>/transactions/<int:id>/',
        GoalTransactionManagerViewSet.as_view({
            'get': 'retrieve',
        }),
        name='goal_transaction-detail'
    ),
]
