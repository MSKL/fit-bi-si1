from main import db


class RaceType(db.Model):
    """Represents a type of the race"""
    __tablename__ = "racetype"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))

    def __init__(self, name):
        self.name = name