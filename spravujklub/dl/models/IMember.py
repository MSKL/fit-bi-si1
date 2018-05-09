class IMember(object):
    """Member interface class. Includes all functions that will be needed by Member class."""

    def is_authenticated(self):
        """This property should return True if this is an anonymous user. (Actual users should return False instead.)"""
        raise NotImplementedError()

    def is_active(self):
        """This property should return True if this is an active user - in addition to being authenticated, they also
        have activated their account, not been suspended, or any condition your application has for rejecting an
        account. Inactive accounts may not log in (without being forced of course)."""
        raise NotImplementedError()

    def is_anonymous(self):
        """Check if the user is anonymous."""
        raise NotImplementedError()

    def get_id(self):
        """This method must return a unicode that uniquely identifies this user, and can be used to load the user from
        the user_loader callback. Note that this must be a unicode - if the ID is natively an int or some other type,
        you will need to convert it to unicode."""
        raise NotImplementedError()
