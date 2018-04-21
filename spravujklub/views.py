from flask import request, render_template, redirect
from flask_login import login_required, login_user, logout_user, current_user
from functions import app_create_user, app_delete_user_by_id, app_login_user
from models.Race import Race
from models.Member import Member
from main import app, db, login_manager
import datetime


@login_manager.user_loader
def load_user(user_id):
    """should take the unicode ID of a user, and return the corresponding user object"""
    return db.session.query(Member).get(user_id)


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
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
    return render_template("index.html", members=Member.query.all(), title="Spravuj Klub Index")


@app.route('/races', methods=['GET'])
@login_required
def races():
    races_query = [Race("Zavod1", "Zavodovice", datetime.date(2018, 1, 8), True),
                   Race("Zavod2", "testtest", datetime.date(2018, 1, 8), False),
                   Race("Zavod3", "Racetown", datetime.date(2018, 1, 8), False),
                   Race("Zavod4", "Zavodnikov", datetime.date(2018, 1, 8), True)]
    # Render the template
    return render_template("races.html", races=races_query)


@app.route('/race_detail', methods=['GET'])
@login_required
def race_detail():
    # TODO: Make race detail page (not editable)
    pass


@app.route('/race_edit', methods=['GET'])
@login_required
def race_edit():
    # TODO: Make race detail page (editable)
    pass


# @app.route('/profile/<user_id>', methods = ['GET', 'POST', 'DELETE'])
# @login_required # TODO: Anybody can view any member's page ATM. NOT TESTED.
# def profile(user_id):
#    if request.method == 'GET':
#        """return the information for <user_id>"""
#    if request.method == 'POST':
#        """modify/update the information for <user_id>"""
#        data = request.form  # a multidict containing POST data
#    if request.method == 'DELETE':
#        """delete user with ID <user_id>"""
#    else:
#        # POST Error 405 Method Not Allowed
#        pass
#
#    return "Not implemented yet."


@app.route('/login', methods=['GET', 'POST'])
def login():
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
