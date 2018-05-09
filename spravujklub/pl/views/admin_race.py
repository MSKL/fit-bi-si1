from flask import request, render_template
from flask_login import login_required, current_user
from spravujklub import app, race_controller


@app.route('/admin_race', methods=['GET'])
@login_required
def admin_race():
    """Admin panel to manage races"""

    # Testing adding to the DB
    name = request.values.get("name")
    date = request.values.get("date")
    deadline = request.values.get("deadline")
    info = request.values.get("info")

    error = None
    if name is not None and date is not None and deadline is not None and info is not None:
        try:
            current_id = current_user.id or -1
            race_controller.add_race(name=name, created_by_user_id=current_id, date=date, deadline=deadline, info=info)
        except Exception as ex:
            error = str(ex)

    # Render the template
    return render_template("admin_race.html", races=race_controller.get_all_races(), title="Race admin", error=error)