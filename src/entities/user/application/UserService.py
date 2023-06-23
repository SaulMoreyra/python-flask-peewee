from typing import Type
from ..domain import UserRepository, UserEntity


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def find_all(self) -> Type[UserEntity]:
        return self.repository.find_all()

    def find_by_id(self, id: int):
        user_find = self.repository.find_by_id(id)
        if user_find:
            return user_find.__data__
        return None

    def create_one(self, **user):
        user_created = self.repository.create_one(**user)
        if user_created:
            return user_created.__data__
        return None
