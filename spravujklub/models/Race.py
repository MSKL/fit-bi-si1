from main import db


class Race(db.Model):
    """class representing the app user"""
    __tablename__ = "races"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=True)
    type = "Sometype"  # TODO
    place = db.Column(db.String(200))
    start_time = db.Column(db.Time)
    organizer = db.Column(db.String(200))
    end_registration = db.Column(db.DateTime)
    disciplines = "Běh, Skok, Hod"  # TODO
    url = db.Column(db.String(200))
    info = db.Column(db.Text)

    def __init__(self, name, date, deadline, created_by_user=None, type=None, place=None, start_time=None,
                 organizer=None, end_registration=None, disciplines=None, url=None, info=None):
        """Name, date, deadline, and created_by_user must be set"""
        self.name = name
        self.type = type
        self.place = place
        self.date = date
        self.start_time = start_time
        self.deadline = deadline
        self.created_by_user_id = created_by_user
        self.organizer = organizer
        self.end_registration = end_registration
        self.disciplines = disciplines
        self.url = url
        self.info = info
        self.user_registered = False

    def set_user_registered(self, val):
        self.user_registered = val
