from flask import request, render_template, redirect, url_for
from spravujklub import race_controller
from datetime import datetime
from dl.database import db
from pl.views.interfaces.ILoginRequiredView import ILoginRequriedView


class RaceEditView(ILoginRequriedView):
    """Page that allows the user to edit a race."""

    def dispatch_request(self, race_id):
        """Render a page that allows the user to login"""

        # Try to get the race from the database. If failed, return to the index with an error.
        try:
            race = race_controller.get_race_by_id(race_id)
        except Exception as ex:
            return redirect(url_for('.index', error=str(ex)))

        name = request.values.get("name")
        date = request.values.get("date")
        deadline = request.values.get("deadline")
        info = request.values.get("info")

        error = None
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
                error = str(ex)

        return render_template("race_edit.html", race=race, error=error)


