from flask import redirect
from flask_login import login_required
from spravujklub import member_controller
from pl.views.interfaces.ILoginRequiredView import ILoginRequriedView


class LogoutView(ILoginRequriedView):
    """Log out the user"""

    def dispatch_request(self):
        """Logs out the current user and then redirects to the index"""
        try:
            member_controller.logout_member()
        except Exception as ex:
            print(str(ex))

        return redirect("/")
