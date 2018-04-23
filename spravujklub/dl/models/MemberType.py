from main import db


class MemberType(db.Model):
    __tablename__ = "membertype"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name
