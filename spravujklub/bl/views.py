from flask import request, render_template, redirect
from flask_login import login_required, logout_user, current_user
from bl.functions import app_create_user, app_delete_user_by_id, app_login_user
from dl.models.Race import Race
from dl.models.Member import Member
from main import app, db, login_manager
import datetime


@login_manager.user_loader
def load_user(user_id):
    """
    Should take the unicode ID of a user, and return the corresponding user object.
    This function if required by the flask_login. Should not be removed.
    """
    return db.session.query(Member).get(user_id)


@app.route('/admin_panel', methods=['GET', 'POST'])
#@login_required
def admin_panel():
    print(current_user.is_authenticated)

    # Testing adding to the DB
    name = request.values.get("name")
    email = request.values.get("mail")
    password = request.values.get("password")

    # Testing deleting from DB
    delete = request.values.get("delete", type=int)

    if name and email and password:
        app_create_user(name=name, email=email, password=password)

    if delete:
        app_delete_user_by_id(delete)

    # Render the template
    return render_template("index.html", members=Member.query.all(), title="Admin panel")


@app.route('/', methods=['GET'])
@login_required
def index():
    races_query2 = [Race(name="Zavod1", date=datetime.date(2018, 1, 8), created_by_user=0, deadline=datetime.date(2018, 1, 7)),
         Race(name="Zavod2", date=datetime.date(2018, 1, 8), created_by_user=0, deadline=datetime.date(2018, 1, 7)),
         Race(name="Zavod3", date=datetime.date(2018, 1, 8), created_by_user=0, deadline=datetime.date(2018, 1, 7)),
         Race(name="Zavod4", date=datetime.date(2018, 1, 8), created_by_user=0, deadline=datetime.date(2018, 1, 7))]

    # Render the template
    return render_template("races.html", races=races_query2, title="Races")


@app.route('/race_detail/<race_id>', methods=['GET'])
@login_required
def race_detail(race_id):
    # TODO: Make race detail page (not editable)
    # TODO: get id from url and query database for race
    testRace =  Race(name="Zavod4",
                     type="pohar",
                     place="Zavodnikov",
                     date=datetime.date(2018, 1, 8),
                     deadline=datetime.date(2018, 1, 7),
                     ).set_user_registered(True)
    return render_template("race_detail.html", race=testRace, userid=1)


@app.route('/race_edit/<race_id>', methods=['GET'])
@login_required
def race_edit(race_id):
    # TODO: get id from url and query database for race
    testRace = Race(name="Zavod4",
                    type="pohar",
                    place="Zavodnikov",
                    date=datetime.date(2018, 1, 8),
                    deadline=datetime.date(2018, 1, 7),
                    ).set_user_registered(True)
    return render_template("race_edit.html", race=testRace, userid=1)


@app.route('/profile/<user_id>', methods = ['GET', 'POST', 'DELETE'])
@login_required
def profile(user_id):
    # TODO: Anybody can view any member's page ATM.

    if request.method == 'GET':
        """return the information for <user_id>"""
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # a multidict containing POST data
        data = request.form
    if request.method == 'DELETE':
        """delete user with ID <user_id>"""
    else:
        # POST Error 405 Method Not Allowed
        pass

    return "Not implemented yet."


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Checks if the user if authotized. If not, redirects him to a login screen."""
    if current_user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            login_mail = request.form.get("login_mail")
            login_password = request.form.get("login_password")
            if login_mail and login_password:
                if app_login_user(login_mail, login_password):
                    return redirect("/")

    return render_template("login.html", title="Login")


@app.route('/logout')
@login_required
def logout():
    """Logs out the current user and then redirects to the index"""
    logout_user()
    return redirect("/")
