from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView


class CustomTokenRefreshView(TokenRefreshView):
    """
    POST /api/auth/refresh/
    body: { "refresh": "..." }
    Rotating yoqilgan — har safar yangi refresh qaytaradi.
    """
    permission_classes = [permissions.AllowAny]
