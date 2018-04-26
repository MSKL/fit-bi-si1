from flask import request, render_template, redirect
from flask_login import current_user
from main import app, member_controller


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Logs the user into the website"""

    # Checks if the user if authotized. If not, redirects him to a login screen.
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
                print(ex)

    return render_template("login.html", title="Login")