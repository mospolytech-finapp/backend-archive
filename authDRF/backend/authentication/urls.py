from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomUserRegistration, CustomUserAuthentication, CustomUserDetails

from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer

@api_view(['GET'])
def get_users(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

urlpatterns = [
    path('api/users/', get_users),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', CustomUserRegistration.as_view(), name='register'),
    path('login/', CustomUserAuthentication.as_view(), name='login'),
    path('user/', CustomUserDetails.as_view(), name='user'),
]
