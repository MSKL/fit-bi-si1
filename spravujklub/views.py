from flask import request, render_template
from entities.Race import Race
from main import app, db
from models import Member
import flask_login
import datetime


@app.route('/', methods=['GET'])
def index():
    name = request.values.get("name")
    email = request.values.get("mail")
    password = request.values.get("password")
    delete = request.values.get("delete")

    if name and email:
        # Create a new member
        new_member = Member(name=name, email=email, password=password)
        # Add it to the database session
        db.session.add(new_member)
        # Commit the change to the DB
        db.session.commit()

    if delete:
        memb = db.session.query(Member).get(delete)
        db.session.delete(memb)
        db.session.commit()

    # Get all members from the DB
    members = Member.query.all()

    # Render the template
    return render_template("index.html", members=members, title="SpravujKlub", user=Member("Lukas", "test@test.cz", "1234"))


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


@app.route('/profile', methods=[ 'GET' ])
def profile():
    # TODO: Make the user's profile page
    return render_template("profile.html", user=Member("Lukas", "test@test.cz", "1234"))


@app.route('/login', methods= [ 'POST' ])
def login():
    # TODO: Make the login page
    pass


@flask_login.login_required
@app.route('/restricted')
def restricted():
    """just a test site to see if the auth works"""
    return "User must be logged in to see this!"
