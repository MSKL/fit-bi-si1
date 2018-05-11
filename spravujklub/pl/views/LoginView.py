from flask import request, render_template, redirect
from flask_login import current_user
from spravujklub import member_controller
from pl.views.interfaces import IDefaultView


class LoginView(IDefaultView):
    """This class handles the login of the user"""

    def dispatch_request(self):
        """Renders the login page"""

        # Checks if the user if authotized. If not, redirects him to a login screen.
        error = None
        if current_user.is_authenticated:
            return redirect("/")
        else:
            login_mail = request.form.get("login_mail")
            login_password = request.form.get("login_password")
            if login_mail is not None and login_password is not None:
                try:
                    member_controller.login_member(login_mail, login_password)
                    return redirect("/")
                except Exception as ex:
                    error = "Přihlášení se nezdařilo"

        return render_template("login.html", title="Login", error=error)


# Catch the errors on import to successfully generate the documentation
try:
    pass
except Exception as ex:
    print(str(ex))