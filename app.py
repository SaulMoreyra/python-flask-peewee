from flask import Flask
from peewee import *
from src.entities.user import UserController
from src.database import init

app = Flask(__name__)
app.config.from_object(__name__)
app.register_blueprint(UserController.bp)

if __name__ == '__main__':
    init.create_tables()
    app.run(debug=True)
