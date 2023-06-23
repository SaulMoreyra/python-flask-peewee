from ...database.config import database
from peewee import *


class BaseEntity(Model):

    def to_dict(self):
        pass

    class Meta:
        database = database
