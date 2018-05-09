from dl import IMemberController
from dl.models import Member
from flask_login import login_user, logout_user
from bl import Crypto


class MemberController(IMemberController):

    def __init__(self, db):
        self.db = db

    def get_all_members(self):
        return Member.query.all()

    def get_member_by_id(self, id):
        member = Member.query.get(id)

        if member is None:
            raise Exception("Member with id %s not found." % str(id))

        return member

    def get_member_by_mail(self, mail):
        return Member.query.filter_by(mail=mail).first()

    def delete_member(self, member):
        self.db.session.delete(member)
        self.db.session.commit()

    def create_member(self, name, mail, password):
        # Generate a salt and hash the password
        password_hash, password_salt = Crypto.generate_password_salt(password)

        # Create a new member
        new_member = Member(name=name, email=mail, password=password_hash, salt=password_salt)

        # Add it to the database session and commit
        self.db.session.add(new_member)
        self.db.session.commit()

    def login_member(self, login_mail, login_password):
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
        logout_user()