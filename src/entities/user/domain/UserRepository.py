from typing import Type
from src.core.domain.repository import BaseRepository
from . import UserEntity


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(repository=UserEntity)
