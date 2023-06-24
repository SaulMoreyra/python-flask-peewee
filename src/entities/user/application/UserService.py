from typing import Type
from ..domain import UserRepository, UserEntity, User
from .UserParser import UserParser


class UserService:
    def __init__(self):
        self.repository = UserRepository()
        self.parser = UserParser()

    def find_all(self) -> Type[UserEntity]:
        users = [user for user in self.repository.find_all()]
        users_dicts = list(map(self.parser.to_dict, users))
        return users_dicts

    def find_by_id(self, id: int):
        user_find = self.repository.find_by_id(id=id)
        return self.parser.to_dict(user_find)

    def create_one(self, user: User):
        user_created = self.repository.create_one(**user.to_dict())
        return self.parser.to_dict(user_created)
