from dl.database import db
from dl.models.IMember import IMember


class Member(db.Model, IMember):
    """Class representing the user of the web application"""

    # The name of the table used in the DB
    __tablename__ = "members"
    __table_args__ = {'extend_existing': True}

    # Member data columns
    #: Unique id of the member
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #: Member's name
    name = db.Column(db.String(50))
    #: Member's email
    email = db.Column(db.String(50), unique=True)
    #: Member's password
    password = db.Column(db.String(50))
    #: Salt for the password
    salt = db.Column(db.String(16))

    #: Race id's that the member takes part in
    races = db.relationship('Race', secondary='ucast_na_zavode')

    #: Races this person created
    created_races = db.relationship('Race', backref='created_by', lazy=True)

    def __init__(self, name, email, password, salt):
        """
        Create a new user with the given parameters.

        :type name: str
        :param name: name of the user
        :type email: str
        :param email: email of the user
        :type password: str
        :param password: password of the user
        :type: salt: str
        :param salt: salt
        """

        self.name = name
        self.email = email
        self.password = password
        self.salt = salt

    def get_id(self):
        """
        Get the id of this user.

        :rtype: int
        :return: user id
        """

        return str(self.id)

    def is_authenticated(self):
        """
        :rtype: bool
        :return: True if the user is anonymous
        """
        pass

    def is_active(self):
        """
        :rtype: bool
        :return: True if this is an active user
        """
        pass

    def is_anonymous(self):
        """
        :rtype: bool
        :return: true if the user is anonymous
        """
        pass
