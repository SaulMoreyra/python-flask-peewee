
class User():
    def __init__(self, username, password, email, join_date, id=None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.join_date = join_date

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "join_date": self.join_date
        }
