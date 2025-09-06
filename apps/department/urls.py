from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.DeparmentCreateAPIView.as_view()),
    path('edit/<int:pk>/', views.DepartmentUpdateAPIView.as_view()),
    path('delete/<int:pk>/', views.DeparmentDeleteAPIView.as_view()),
    path('retrieve/<int:pk>/', views.DepartmentRetrieveAPIView.as_view()),
    path('list/', views.DepartmentOrganizationListAPIView.as_view()),
    path('<int:department_id>/employees/', views.DepartmentEmployeesAPIView.as_view()),
]

