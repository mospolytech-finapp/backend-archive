from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from authentication.views import UserViewSet

urlpatterns = [
    path('token/', obtain_auth_token, name='token'),
    path(
        'registration/',
        UserViewSet.as_view(
            {'post': 'create'}
        ),
        name='registration'
    ),
    #path(
    #    'user/',
    #    UserViewSet.as_view({
    #        'get': 'retrieve',
    #        'patch': 'partial_update',
    #    }),
    #    name='user'
    #),
]
