from flask import request, render_template, redirect
from flask_login import login_required, current_user
from dl.models.Race import Race
from main import app, member_controller, race_controller
from database import db
from datetime import datetime


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Logs the user into the website"""

    # Checks if the user if authotized. If not, redirects him to a login screen.
    if current_user.is_authenticated:
        return redirect("/")
    else:
        login_mail = request.form.get("login_mail")
        login_password = request.form.get("login_password")
        if login_mail is not None and login_password is not None:
            try:
                member_controller.login_member(login_mail, login_password)
                return redirect("/")
            except Exception as ex:
                print(ex)

    return render_template("login.html", title="Login")


@app.route('/logout')
@login_required
def logout():
    """Logs out the current user and then redirects to the index"""
    try:
        member_controller.logout_member()
    except Exception as ex:
        print(str(ex))

    return redirect("/")


@app.route('/', methods=['GET'])
@login_required
def index():
    """Index shows the upcoming races"""
    races_from_db = Race.query.all()
    return render_template("races.html", races=races_from_db, title="Nadcházející závody")


@app.route('/admin_member', methods=['GET'])
def admin_member():
    """Admin panel to manage members"""
    name = request.values.get("name")
    email = request.values.get("mail")
    password = request.values.get("password")
    delete_id = request.values.get("delete")

    if name is not None and email is not None:
        try:
            member_controller.create_member(name=name, mail=email, password=password)
        except Exception as ex:
            print(str(ex))

    if delete_id is not None:
        try:
            delete_id = int(delete_id)
            member_to_delete = member_controller.get_member_by_id(delete_id)
            member_controller.delete_member(member_to_delete)
        except Exception as ex:
            print(str(ex))

    # Render the template
    return render_template("admin_member.html", members=member_controller.get_all_members(), title="Member admin")


@app.route('/admin_race', methods=['GET'])
@login_required
def admin_race():
    """Admin panel to manage races"""

    # Testing adding to the DB
    name = request.values.get("name")
    date = request.values.get("date")
    deadline = request.values.get("deadline")
    info = request.values.get("info")

    if name is not None and date is not None and deadline is not None and info is not None:
        try:
            current_id = current_user.id or -1
            race_controller.add_race(name=name, created_by_user_id=current_id, date=date, deadline=deadline, info=info)
        except Exception as ex:
            print(str(ex))

    # Render the template
    return render_template("admin_race.html", races=race_controller.get_all_races(), title="Race admin")


@app.route('/race_detail/<race_id>', methods=['GET'])
@login_required
def race_detail(race_id):
    try:
        race = race_controller.get_race_by_id(race_id)
    except Exception as ex:
        print(str(ex))
        return redirect("/")

    member_signup_id = request.values.get("member_signup")
    member_signoff_id = request.values.get("member_signoff")

    if member_signup_id is not None:
        try:
            member_signup_id = int(member_signup_id)
            member_to_signup = member_controller.get_member_by_id(member_signup_id)
            race.add_member(member_to_signup)
        except Exception as ex:
            print(str(ex))

    if member_signoff_id is not None:
        try:
            member_signoff_id = int(member_signoff_id)
            member_to_signoff = member_controller.get_member_by_id(member_signoff_id)
            race.remove_member(member_to_signoff)
        except Exception as ex:
            print(str(ex))

    return render_template("race_detail.html", race=race)


@app.route('/race_edit/<race_id>', methods=['GET'])
@login_required
def race_edit(race_id):
    try:
        race = race_controller.get_race_by_id(race_id)
    except Exception as ex:
        print(str(ex))
        return redirect("/")

    name = request.values.get("name")
    date = request.values.get("date")
    deadline = request.values.get("deadline")
    info = request.values.get("info")

    if name is not None and date is not None and deadline is not None and info is not None:
        try:
            # Convert the parameters
            date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            deadline = datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')

            # Update the values
            race.name = name
            race.date = date
            race.deadline = deadline
            race.info = info

            # Commit the session TODO: Solve this to make it somewhere else
            db.session.commit()

            return redirect("/race_detail/%s" % str(race_id))
        except Exception as ex:
            print(str(ex))

    return render_template("race_edit.html", race=race)


@app.route('/profile/<user_id>', methods = ['GET', 'POST', 'DELETE'])
@login_required
def profile(user_id):
    # TODO: Anybody can view any member's page ATM.

    if request.method == 'GET':
        """return the information for <user_id>"""
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
    if request.method == 'DELETE':
        """delete user with ID <user_id>"""

    return "Not implemented yet."

