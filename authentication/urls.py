from django.urls import path
from .views import RegisterView, LoginView
#from .views import HomeView

urlpatterns = [
    #path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
