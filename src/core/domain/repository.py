from typing import List
from peewee import Model


class BaseRepository:
    def __init__(self, repository: Model):
        self.repository = repository

    def create_one(self, **entity) -> Model:
        return self.repository.create(**entity)

    def find_by_id(self, **data) -> Model:
        return self.repository.get_or_none(**data)

    def find_all(self) -> List[Model]:
        return self.repository.select()
