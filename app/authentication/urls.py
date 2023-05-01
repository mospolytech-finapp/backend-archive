from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from authentication.views import RegistrationView

urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('token/', obtain_auth_token)
]