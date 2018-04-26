from flask import request, render_template, redirect
from flask_login import login_required
from main import app, member_controller, race_controller


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