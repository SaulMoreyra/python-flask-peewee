import os
from peewee import *
from dotenv import load_dotenv

load_dotenv()

DATABASE = os.environ.get('DATABASE')
database = SqliteDatabase(DATABASE)
