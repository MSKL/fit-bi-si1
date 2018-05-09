from flask import render_template
from flask_login import login_required
from spravujklub import app
from dl.models.Race import Race


@app.route('/', methods=['GET'])
@login_required
def index():
    """Shows the upcoming races"""
    # Get the races
    races_from_db = Race.query.all()

    # Sort them based on the date
    races_from_db.sort(key=lambda r: r.date)

    # Draw the page
    return render_template("races.html", races=races_from_db, title="Nadcházející závody")