from flask import request, render_template, redirect
from flask_login import login_required, login_user, logout_user
from entities.Race import Race
from main import app, db
from models import Member
from crypto import hash_password, generate_salt
import datetime
from functions import app_login_user, app_create_user, app_delete_user_by_id


@app.route('/', methods=['GET', 'POST'])
def index():
    # Testing adding to the DB
    name = request.values.get("name")
    email = request.values.get("mail")
    password = request.values.get("password")
    # Testing deleting from DB
    delete = request.values.get("delete", type=int)
    # Testing login
    login_mail = request.values.get("login_mail")
    login_password = request.values.get("login_password")

    if name and email and password:
        app_create_user(name=name, email=email, password=password)

    if delete:
        app_delete_user_by_id(delete)

    if login_mail and login_password:
        app_login_user(login_mail=login_mail, login_password=login_password)

    # Render the template
    return render_template("index.html", members=Member.query.all(), title="Spravuj Klub Index")


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


@app.route('/restricted')
@login_required
def restricted():
    """just a test site to see if the auth works"""
    return "User is now logged in. Others can't see this.!"


@app.route('/logout')
def logout():
    """Logs out the current user and then redirects to the index"""
    logout_user()
    return redirect("/")