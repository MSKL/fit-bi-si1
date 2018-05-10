from flask import request, render_template, redirect
from flask_login import current_user
from spravujklub import app, member_controller
from flask.views import View


class Login(View):
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


try:
    app.add_url_rule('/login/', view_func=Login.as_view('login'), methods=['GET', 'POST'])
except Exception as ex:
    print(str(ex))