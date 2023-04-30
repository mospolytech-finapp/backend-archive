from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionManagerViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionManagerViewSet, 'transaction')

urlpatterns = [
    path('', include(router.urls)),
]
