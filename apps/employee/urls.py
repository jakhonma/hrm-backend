from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.EmployeeCreateAPIView.as_view()),
    path('update/<int:pk>/', views.EmployeeUpdateAPIView.as_view()),
    path('delete/<int:pk>/', views.EmployeeDeleteAPIView.as_view()),
    path('list-head/<int:department_id>/', views.EmployeeDepartmentAddAPIView.as_view()),
]
