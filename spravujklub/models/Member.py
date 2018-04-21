from main import db


class Member(db.Model):
    """class representing the app user"""
    __tablename__ = "members"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    salt = db.Column(db.String(16))

    def __init__(self, name, email, password, salt):
        self.name = name
        self.email = email
        self.password = password
        self.salt = salt

    def is_authenticated(self):
        """This property should return True if this is an anonymous user. (Actual users should return False instead.)"""
        pass

    def is_active(self):
        """This property should return True if this is an active user - in addition to being authenticated, they also
        have activated their account, not been suspended, or any condition your application has for rejecting an
        account. Inactive accounts may not log in (without being forced of course)."""
        pass

    def is_anonymous(self):
        pass

    def get_id(self):
        """This method must return a unicode that uniquely identifies this user, and can be used to load the user from
        the user_loader callback. Note that this must be a unicode - if the ID is natively an int or some other type,
        you will need to convert it to unicode."""
        return str(self.id)
