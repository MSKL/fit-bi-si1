from flask import request, render_template, redirect
from flask_login import login_required, current_user
from spravujklub import app, member_controller, race_controller


@app.route('/logout')
@login_required
def logout():
    """Logs out the current user and then redirects to the index"""
    try:
        member_controller.logout_member()
    except Exception as ex:
        print(str(ex))

    return redirect("/")