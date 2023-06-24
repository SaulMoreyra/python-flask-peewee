from ...database.config import database
from peewee import *


class BaseEntity(Model):
    class Meta:
        database = database
