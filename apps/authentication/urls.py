from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refresh/', views.CustomTokenRefreshView.as_view(), name="token_refresh"),
    path('logout/', views.LogoutView.as_view(), name="token_logout"),
]

