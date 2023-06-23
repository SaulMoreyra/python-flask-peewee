from typing import Generic, TypeVar, List

T = TypeVar('T')


class BaseRepository(Generic[T]):
    def __init__(self, repository: T):
        self.repository = repository

    def create_one(self, **entity) -> T:
        return self.repository.create(**entity)

    def find_by_id(self, id: int) -> T:
        return self.repository.get_or_none(id=id)

    def find_all(self) -> List[T]:
        return self.repository.select().execute()
