from flask_login import login_user
from main import db
from models import Member
from crypto import generate_salt, hash_password


def app_login_user(login_password, login_mail):
    some_user = db.session.query(Member).filter(Member.email == login_mail).first()
    if not some_user:
        print("User not found")
    else:
        hashed = hash_password(login_password, some_user.salt)
        if hashed == some_user.password:
            login_user(some_user)
            print("Logged in user %s" % some_user.email)


def app_logout_user():
    pass


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
    memb = db.session.query(Member).get(id)
    db.session.delete(memb)
    db.session.commit()