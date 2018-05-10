from flask import render_template, redirect, url_for
from flask_login import login_required
from spravujklub import app, member_controller
from flask.views import View


class Profile(View):
    """The profile page"""

    decorators = [login_required]

    def dispatch_request(self, user_id):
        """Get the user and render the page"""

        # Get the member and check if exists
        member = None
        try:
            member = member_controller.get_member_by_id(user_id)
        except Exception as ex:
            return redirect(url_for('.index', error=str(ex)))

        return render_template("profile.html", member=member)


try:
    app.add_url_rule('/profile/<user_id>', view_func=Profile.as_view('profile'))
except Exception as ex:
    print(str(ex))





