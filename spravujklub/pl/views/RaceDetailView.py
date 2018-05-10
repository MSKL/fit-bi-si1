from flask import request, render_template, redirect, url_for
from spravujklub import app, member_controller, race_controller
from pl.views.interfaces.ILoginRequiredView import ILoginRequriedView


class RaceDetailView(ILoginRequriedView):
    """Display a detail of a race"""

    def dispatch_request(self, race_id):
        """View a race with and id and render the page"""

        # Try to get the race from the database. If failed, return to the index with an error.
        try:
            race = race_controller.get_race_by_id(race_id)
        except Exception as ex:
            return redirect(url_for('.index', error=str(ex)))

        # Error message if any
        error = None

        # If the member signup is passed
        member_signup_id = request.values.get("member_signup")
        if member_signup_id is not None:
            try:
                member_signup_id = int(member_signup_id)
                member_to_signup = member_controller.get_member_by_id(member_signup_id)
                race.add_member(member_to_signup)
            except Exception as ex:
                error = "Na závod se již není možné přihlásit."

        # If the member signoff is passed
        member_signoff_id = request.values.get("member_signoff")
        if member_signoff_id is not None:
            try:
                member_signoff_id = int(member_signoff_id)
                member_to_signoff = member_controller.get_member_by_id(member_signoff_id)
                race.remove_member(member_to_signoff)
            except Exception as ex:
                error = "Ze závodu se již není možné odhlásit."

        return render_template("race_detail.html", race=race, error=error)


try:
    app.add_url_rule('/race_detail/<race_id>', view_func=RaceDetailView.as_view('race_detail'), methods=['GET'])
except Exception as ex:
    print(str(ex))
