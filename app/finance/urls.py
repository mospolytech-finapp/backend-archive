from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionManagerViewSet, CategoryManagerViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionManagerViewSet, 'transaction')
router.register(r'categories', CategoryManagerViewSet, 'category')

urlpatterns = [
    path('', include(router.urls)),
]
