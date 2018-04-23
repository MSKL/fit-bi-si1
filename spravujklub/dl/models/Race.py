from main import db

# many to many relationship between race and a member
tags = db.Table('ucast_na_zavode',
    db.Column('member_id', db.Integer, db.ForeignKey('members.id'), primary_key=True),
    db.Column('race_id', db.Integer, db.ForeignKey('races.id'), primary_key=True)
)


class Race(db.Model):
    """class representing the app user"""
    __tablename__ = "races"
    # Race data columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    info = db.Column(db.Text)
    # Foreign key to the member that created this race
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    # Members that are registered to the race
    members = db.relationship('Member', secondary='ucast_na_zavode')


    def __init__(self, name, date, deadline, created_by_user=None, info=None):
        """Name, date, deadline, and created_by_user must be set"""
        self.name = name
        self.date = date
        self.deadline = deadline
        self.created_by_user_id = created_by_user
        self.info = info

    def add_member(self, member_id):
        """Adds a member to the race"""
        pass