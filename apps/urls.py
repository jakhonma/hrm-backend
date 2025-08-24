from django.urls import path, include


urlpatterns = [
    path('department/', include('apps.department.urls')),
    path('employee/', include('apps.employee.urls')),
]

