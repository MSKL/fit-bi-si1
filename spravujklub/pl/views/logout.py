from flask import redirect
from flask_login import login_required
from spravujklub import app, member_controller
from flask.views import View


class Logout(View):
    """Log out the user"""

    decorators = [login_required]

    def dispatch_request(self):
        """Logs out the current user and then redirects to the index"""
        try:
            member_controller.logout_member()
        except Exception as ex:
            print(str(ex))

        return redirect("/")


try:
    app.add_url_rule('/logout', view_func=Logout.as_view('logout'), methods=['GET'])
except Exception as ex:
    print(str(ex))