from flask import render_template, redirect, url_for
from spravujklub import member_controller
from pl.views.interfaces.ILoginRequiredView import ILoginRequriedView


class ProfileView(ILoginRequriedView):
    """The profile page"""

    def dispatch_request(self, user_id):
        """Get the user and render the page"""

        # Get the member and check if exists
        member = None
        try:
            member = member_controller.get_member_by_id(user_id)
        except Exception as ex:
            return redirect(url_for('.index', error=str(ex)))

        return render_template("profile.html", member=member)







