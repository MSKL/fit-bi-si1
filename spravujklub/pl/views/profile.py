from flask import render_template, redirect, url_for
from flask_login import login_required
from main import app, member_controller


@app.route('/profile/<user_id>', methods=['GET', 'POST', 'DELETE'])
@login_required
def profile(user_id):
    """Views the information about the user's profile"""
    # TODO: Anybody can view any member's page ATM.
    # TODO: Use the POST and DELETE methods
    # TODO: Make the profile editable

    """
    if request.method == 'GET':
        # return the information for <user_id>
    if request.method == 'POST':
        # modify/update the information for <user_id>
    if request.method == 'DELETE':
        # delete user with ID <user_id>
    """

    # Get the member and check if exists
    member = None
    try:
        member = member_controller.get_member_by_id(user_id)
    except Exception as ex:
        return redirect(url_for('.index', error=str(ex)))

    return render_template("profile.html", member=member)
