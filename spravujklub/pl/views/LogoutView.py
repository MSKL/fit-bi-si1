from flask import redirect
from flask_login import login_required
from spravujklub import app, member_controller
from pl.views.interfaces.ILoginRequiredView import ILoginRequriedView


class LogoutView(ILoginRequriedView):
    """Log out the user"""

    decorators = [login_required]

    def dispatch_request(self):
        """Logs out the current user and then redirects to the index"""
        try:
            member_controller.logout_member()
        except Exception as ex:
            print(str(ex))

        return redirect("/")


# Catch the errors on import to successfully generate the documentation
try:
    app.add_url_rule('/logout', view_func=LogoutView.as_view('logout'), methods=['GET'])
except Exception as ex:
    print(str(ex))