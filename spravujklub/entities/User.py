"""
FLASK_LOGIN info:

Your User Class
The class that you use to represent users needs to implement these properties and methods:

is_authenticated
This property should return True if the user is authenticated, i.e. they have provided valid credentials.
(Only authenticated users will fulfill the criteria of login_required.)

is_active
This property should return True if this is an active user - in addition to being authenticated, they also have
activated their account, not been suspended, or any condition your application has for rejecting an account.
Inactive accounts may not log in (without being forced of course).

is_anonymous
This property should return True if this is an anonymous user. (Actual users should return False instead.)

get_id()
This method must return a unicode that uniquely identifies this user, and can be used to load the user from the
user_loader callback. Note that this must be a unicode - if the ID is natively an int or some other type, you will need
to convert it to unicode.
"""


class User:
    id = 1

    def __init__(self, name, email):
        self.id = User.id
        self.name = name
        self.email = email
        User.id += 1
