from ..domain import UserEntity, User


class UserParser:
    def to_dict(self, user: UserEntity):
        if user is None:
            return None
        user_dict = user.__data__
        user_model = User(**user_dict)
        return user_model.to_json()
