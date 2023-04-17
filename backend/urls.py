from django.urls import path, include
from drf_spectacular.views import \
        SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    # Docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api/auth/', include('authentication.urls')),
]
