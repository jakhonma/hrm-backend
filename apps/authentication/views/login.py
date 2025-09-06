from rest_framework import permissions
from rest_framework.throttling import ScopedRateThrottle


from rest_framework import generics, response, status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from apps.users.models import User
from apps.authentication.serializers import LoginSerializer


class LoginAPIView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def get_serializer_class(self):
        serializer = LoginSerializer
        return serializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return response.Response(
            serializer.validated_data,
            status=status.HTTP_200_OK
        )


# class LoginTokenObtainPairView(TokenObtainPairView):
#     """
#     POST /api/auth/login/
#     body: { "username": "...", "password": "..." }
#     """
#     serializer_class = CustomTokenObtainPairSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = "login"
#     permission_classes = [permissions.AllowAny]