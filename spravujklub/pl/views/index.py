from flask import render_template
from flask_login import login_required
from main import app
from dl.models.Race import Race


@app.route('/', methods=['GET'])
@login_required
def index():
    """Index shows the upcoming races"""
    races_from_db = Race.query.all()
    return render_template("races.html", races=races_from_db, title="Nadcházející závody")