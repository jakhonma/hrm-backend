from rest_framework import permissions
from rest_framework.throttling import ScopedRateThrottle
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.authentication.serializers import CustomTokenObtainPairSerializer


class LoginTokenObtainPairView(TokenObtainPairView):
    """
    POST /api/auth/login/
    body: { "username": "...", "password": "..." }
    """
    serializer_class = CustomTokenObtainPairSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "login"
    permission_classes = [permissions.AllowAny]