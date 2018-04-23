from bl.crypto import generate_salt, hash_password
from dl.IMemberController import IMemberController
from dl.models.Member import Member
from database import db
from flask_login import login_user, logout_user


class MemberController(IMemberController):

    def __init__(self, db):
        self.db = db

    def get_member_by_id(self, id):
        return Member.query.get(id)

    def get_member_by_mail(self, mail):
        return Member.query.filter_by(mail=mail).first()

    def delete_member(self, member):
        member = db.session.query(Member).get(id)
        db.session.delete(member)
        db.session.commit()

    def create_member(self, member):
        db.session.add(member)
        db.session.commit()

    def create_member(self, name, mail, password):
        # Generate a salt and hash the password
        password_salt = generate_salt(16)
        password_hash = hash_password(password, password_salt)

        # Create a new member
        new_member = Member(name=name, email=mail, password=password_hash, salt=password_salt)

        # Add it to the database session and commit
        db.session.add(new_member)
        db.session.commit()

    def login_member(self, login_mail, login_password):
        if login_mail is not None and login_password is not None:
            user_to_login = db.session.query(Member).filter(Member.email == login_mail).first()
            if user_to_login:
                hashed = hash_password(login_password, user_to_login.salt)
                if hashed == user_to_login.password:
                    login_user(user_to_login)
                    return
                else:
                    raise Exception("Password does not match.")
            else:
                raise Exception("Mail not found.")
        else:
            raise Exception("Mail or password is empty.")

    def logout_member(self):
        logout_user()