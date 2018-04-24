from database import db
from dl.models.IMember import IMember


class Member(db.Model, IMember):
    """class representing the app user"""
    __tablename__ = "members"
    # Member data columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    salt = db.Column(db.String(16))
    # Race id's that the member takes part in
    races = db.relationship('Race', secondary='ucast_na_zavode')
    # Races this person created
    created_races = db.relationship('Race', backref='created_by', lazy=True)

    def __init__(self, name, email, password, salt):
        self.name = name
        self.email = email
        self.password = password
        self.salt = salt

    def is_authenticated(self):
        pass

    def is_active(self):
        pass

    def is_anonymous(self):
        pass

    def get_id(self):
        return str(self.id)
