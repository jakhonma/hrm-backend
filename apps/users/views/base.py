from apps.users.serializers import UserSerializer
from apps.users.services import UserService


class BaseUserAPIView:
    serializer_class = UserSerializer
    services = UserService()
