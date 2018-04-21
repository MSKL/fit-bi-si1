from flask import request, render_template, redirect
from entities.Race import Race
from main import app, db
from models import Member
import flask_login
import datetime


@app.route('/', methods=['GET'])
def index():
    # Testing adding to the DB
    name = request.values.get("name")
    email = request.values.get("mail")
    password = request.values.get("password")
    # Testing deleting from DB
    delete = request.values.get("delete")
    # Testing login
    login_mail = request.values.get("login_mail")
    login_password = request.values.get("login_password")

    if name and email:
        # Create a new memberą
        new_member = Member(name=name, email=email, password=password)
        # Add it to the database session
        db.session.add(new_member)
        # Commit the change to the DB
        db.session.commit()

    if delete:
        memb = db.session.query(Member).get(delete)
        db.session.delete(memb)
        db.session.commit()

    if login_mail and login_password:
        some_user = db.session.query(Member).filter(Member.email == login_mail).first()
        if not some_user:
            print("User not found")
        else:
            if login_password == some_user.password:
                flask_login.login_user(some_user)
                print("Logged in user %s" % some_user.email)

    # Get all members from the DB
    members = Member.query.all()

    # Render the template
    return render_template("index.html", members=members, title="SpravujKlub")


@app.route('/races', methods=['GET'])
def races():
    races = []
    races.append(Race("Zavod1", "Zavodovice", datetime.date(2018, 1,8), True))
    races.append(Race("Zavod2", "testtest", datetime.date(2018, 1,8), False))
    races.append(Race("Zavod3", "Racetown", datetime.date(2018, 1,8), False))
    races.append(Race("Zavod4", "Zavodnikov", datetime.date(2018, 1,8), True))
    # Render the template
    return render_template("races.html", races=races, user=Member("Lukas", "test@test.cz", "1234"))


@app.route('/race_detail', methods=['GET'])
def race_detail():
    # TODO: Make race detail page (editable)
    pass


@app.route('/profile', methods=['GET'])
def profile():
    # TODO: Make the user's profile page
    return render_template("profile.html", user=Member("Lukas", "test@test.cz", "1234"))


@app.route('/login', methods= ['POST'])
def login():
    # TODO: Make the login page
    pass


@flask_login.login_required
@app.route('/restricted')
def restricted():
    """just a test site to see if the auth works"""
    return "User must be logged in to see this!"


@app.route('/logout')
def logout():
    """Logs out the current user and then redirects to the index"""
    flask_login.logout_user()
    return redirect("/")