from django.urls import path, include


urlpatterns = [
    path('api/auth/', include('authentication.urls')),
    path('api/finance/', include('finance.urls')),
]
