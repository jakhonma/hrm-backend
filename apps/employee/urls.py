from django.urls import path
from . import views

urlpatterns = [
    path('list-head/', views.EmployeeDepartmentAddAPIView.as_view()),
]

