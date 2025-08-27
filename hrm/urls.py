from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # API endpoints
    path('api/v1/', include('apps.urls')),

    # Schema & Docs
    path("schema/", SpectacularAPIView.as_view(), name="schema"),  # OpenAPI schema (.json)
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    # path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
