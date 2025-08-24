from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.DeparmentCreateAPIView.as_view()),
    path('list/', views.DepartmentOrganizationListAPIView.as_view()),
]

