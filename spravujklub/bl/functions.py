from flask_login import login_user
from main import db
from dl.models.Member import Member
from bl.crypto import generate_salt, hash_password


def app_login_user(login_mail, login_password):
    user_to_login = db.session.query(Member).filter(Member.email == login_mail).first()
    if user_to_login:
        hashed = hash_password(login_password, user_to_login.salt)
        if hashed == user_to_login.password:
            login_user(user_to_login)
            return True
    return False


def app_create_user(name, email, password):
    # Generate a salt and hash the password
    password_salt = generate_salt(16)
    password_hash = hash_password(password, password_salt)

    # Create a new member
    new_member = Member(name=name, email=email, password=password_hash, salt=password_salt)

    # Add it to the database session and commit
    db.session.add(new_member)
    db.session.commit()


def app_delete_user_by_id(id):
    try:
        member = db.session.query(Member).get(id)
        db.session.delete(member)
        db.session.commit()
    except Exception as ex:
        print(str(ex))