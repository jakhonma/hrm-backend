from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


class LogoutView(APIView):
    """
    POST /api/auth/logout/
    body: { "refresh": "..." }
    Refresh tokenni blacklist qiladi.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh = request.data.get("refresh")
        if not refresh:
            return Response({"detail": "refresh is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh)
            token.blacklist()
        except TokenError:
            return Response({"detail": "Invalid or expired refresh token"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Logged out"}, status=status.HTTP_205_RESET_CONTENT)
