from main import db


class Race(db.Model):
    """class representing the app user"""
    __tablename__ = "races"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=True)
    info = db.Column(db.Text)

    def __init__(self, name, date, deadline, created_by_user=None, info=None):
        """Name, date, deadline, and created_by_user must be set"""
        self.name = name
        self.date = date
        self.deadline = deadline
        self.created_by_user_id = created_by_user
        self.info = info

