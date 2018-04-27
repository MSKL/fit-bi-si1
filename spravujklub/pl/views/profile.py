from flask import request, render_template
from flask_login import login_required
from main import app, member_controller


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

    member = member_controller.get_member_by_id(user_id)
    return render_template("profile.html", member=member)
