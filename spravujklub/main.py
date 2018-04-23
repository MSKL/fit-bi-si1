from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


# The flask application
app = Flask("__name__")
Bootstrap(app)

# Setup the config from file
app.config.from_pyfile("config/config_app.py")

# Setup the login manager and init
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """
    Should take the unicode ID of a user, and return the corresponding user object.
    This function if required by the flask_login. Should not be removed.
    """
    from dl.models.Member import Member
    return Member.query.get(user_id)


if __name__ == '__main__':
    # Import the render views after setting up the application
    from views import *
    from config import config_host
    from database import db

    # Register the app in the database
    db.init_app(app)

    # Run the application
    app.run(host=config_host.host, port=config_host.port)
