from .config import database
# from src.entities.message.domain.MessageModel import Message
# from src.entities.relationship.domain.RelationshipModel import Relationship
from src.entities.user import UserEntity

def create_tables():
    with database:
        database.create_tables([UserEntity])