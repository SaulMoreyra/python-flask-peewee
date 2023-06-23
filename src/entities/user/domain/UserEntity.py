from peewee import *
from src.core.domain.entity import BaseEntity


class UserEntity(BaseEntity):
    id = AutoField()
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()

    class Meta:
        table_name = 'user'
