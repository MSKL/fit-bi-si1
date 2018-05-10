import datetime

from dl.database import db
from dl.models.IRace import IRace

# many to many relationship between race and a member
try:
    tags = db.Table('ucast_na_zavode',
        db.Column('member_id', db.Integer, db.ForeignKey('members.id'), primary_key=True),
        db.Column('race_id', db.Integer, db.ForeignKey('races.id'), primary_key=True)
    )
except Exception as ex:
    print(str(ex))


class Race(db.Model, IRace):
    """Class representing a single race"""

    # Name of the table
    __tablename__ = "races"
    __table_args__ = {'extend_existing': True}

    # Race data columns
    #: Unique race ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #: Name of the race
    name = db.Column(db.String(100), nullable=False)
    #: Datetime of the race
    date = db.Column(db.DateTime, nullable=False)
    #: Deadline of the race signup
    deadline = db.Column(db.DateTime, nullable=False)
    #: Information about the race
    info = db.Column(db.Text)

    #: Foreign key to the member that created this race
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('members.id'))

    #: Members that are registered to the race
    members = db.relationship('Member', secondary='ucast_na_zavode')

    def __init__(self, name, date, deadline, created_by_user=None, info=None):
        """
        Create a new Race with given parameters.

        :type name: str
        :param name: name of the race
        :type date: datetime
        :param date: date of the race
        :type deadline: datetime
        :param deadline: deadline of the race applications
        :type created_by_user: User
        :param created_by_user: user that created the race
        :type info: str
        :param info: information about the race
        """

        self.name = name
        self.date = date
        self.deadline = deadline
        self.created_by_user_id = created_by_user
        self.info = info

    def add_member(self, member):
        """
        Add a new race to the database.

        :type member: Race
        :param member: new race to be added
        """

        if datetime.datetime.now() > self.deadline:
            raise Exception
        self.members.append(member)
        db.session.commit()

    def remove_member(self, member):
        """
        Remove a race from the database.

        :type member: Race
        :param member: race to be removed from the database
        """

        if datetime.datetime.now() > self.deadline:
            raise Exception
        self.members.remove(member)
        db.session.commit()
