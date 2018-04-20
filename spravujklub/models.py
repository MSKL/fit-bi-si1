from main import db


class Member(db.Model):
    """class representing the app user"""
    __tablename__ = "members"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
