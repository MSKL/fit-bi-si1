from flask import render_template
from flask_login import login_required
from spravujklub import app
from dl.models.Race import Race
from flask.views import View


class Index(View):
    """Index of the website contains upcoming races."""

    decorators = [login_required]

    def dispatch_request(self):
        """Renders the intdex page and shows upcoming races"""
        # Get the races
        races_from_db = Race.query.all()

        # Sort them based on the date
        races_from_db.sort(key=lambda r: r.date)

        # Draw the page
        return render_template("races.html", races=races_from_db, title="Nadcházející závody")


try:
    app.add_url_rule('/', view_func=Index.as_view('index'), methods=['GET'])
except Exception as ex:
    print(str(ex))
