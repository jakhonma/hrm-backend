from apps.users.repository import UserRepository
from orm import BaseService


class UserService(BaseService):
    repository = UserRepository
