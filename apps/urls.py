from django.urls import path, include


urlpatterns = [
    path('organization/', include('apps.organization.urls')),
]

