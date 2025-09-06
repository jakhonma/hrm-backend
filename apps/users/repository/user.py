from orm import BaseRepository
from apps.users.models import User


class UserRepository(BaseRepository):
    model = User
