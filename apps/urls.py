from django.urls import path, include


urlpatterns = [
    path('auth/', include('apps.authentication.urls')),
    path('user/', include('apps.users.urls')),
    path('department/', include('apps.department.urls')),
    path('employee/', include('apps.employee.urls')),
]

