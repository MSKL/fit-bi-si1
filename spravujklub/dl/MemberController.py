from dl import IMemberController
from dl.models import Member
from flask_login import login_user, logout_user
from bl import Crypto


class MemberController(IMemberController):
    """Database controller for Member objects."""

    def __init__(self, db):
        """
        Initialise the controller with a reference to the database.

        :param db: database
        """

        self.db = db

    def get_all_members(self):
        """
        Get all members stored in the database.

        :rtype: list
        :return: return all members stored in the database
        """

        return Member.query.all()

    def get_member_by_id(self, id):
        """
        Get a member by his ID.

        :type param: int
        :param id: id of the user
        :rtype: Member
        :return: member with given id
        """

        member = Member.query.get(id)

        if member is None:
            raise Exception("Member with id %s not found." % str(id))

        return member

    def get_member_by_mail(self, mail):
        """
        Get a member by his email.

        :type mail: str
        :param mail: email of the member
        :rtype: Member
        :return: member with given email
        """

        return Member.query.filter_by(mail=mail).first()

    def delete_member(self, member):
        """
        Delete a member from the database.

        :type member: Member
        :param member: member to be deleted
        """

        self.db.session.delete(member)
        self.db.session.commit()

    def create_member(self, name, mail, password):
        """
        Create a member with given information.

        :type name: str
        :param name: name of the member
        :type mail: str
        :param mail: email of the member
        :type password: str
        :param password: password of the member
        """

        # Generate a salt and hash the password
        password_hash, password_salt = Crypto.generate_password_salt(password)

        # Create a new member
        new_member = Member(name=name, email=mail, password=password_hash, salt=password_salt)

        # Add it to the database session and commit
        self.db.session.add(new_member)
        self.db.session.commit()

    def login_member(self, login_mail, login_password):
        """
        Try to login a member with given mail and password.

        :type login_mail: str
        :param login_mail: login email
        :type login_password: str
        :param login_password: login password
        """

        user_to_login = self.db.session.query(Member).filter(Member.email == login_mail).first()
        if user_to_login:
            hashed = Crypto.hash_password(login_password, user_to_login.salt)
            if hashed == user_to_login.password:
                login_user(user_to_login)
                return
            else:
                raise Exception("Password does not match.")
        else:
            raise Exception("Mail not found.")

    def logout_member(self):
        """
        Logout the member that is currently logged in.
        """

        logout_user()