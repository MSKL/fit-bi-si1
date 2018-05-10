"""
Top level module responsible for creating the application.
"""

from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import os

from dl.database import db

# The flask application
template_path = os.path.dirname(__file__) + "/pl/templates"
app = Flask("__name__", template_folder=template_path)  #: Create a flask app
Bootstrap(app)                                          #: Register the bootstrap module

# Setup the _config from file
config_path = os.path.dirname(__file__) + "/_config/config_app.py"
app.config.from_pyfile(config_path)                     #: Path to the app configuration file

# Setup the login manager and init
login_manager = LoginManager()                          #: Login manager
login_manager.login_view = 'login'                      #: Name of the login view
login_manager.init_app(app)

# Setup the DB controllers
from dl.MemberController import MemberController
from dl.RaceController import RaceController

member_controller = MemberController(db)                #: DB member controller
race_controller = RaceController(db)                    #: DB race controller

# Import the views
from pl.views import *


@login_manager.user_loader
def load_user(user_id):
    """
    :type user_id: int
    :param user_id:

    Should take the unicode ID of a user, and return the corresponding user object.
    This function if required by the flask_login. Should not be removed.
    """

    from dl.models.Member import Member
    return Member.query.get(user_id)


def run():
    """Run the application"""

    # Import the config and db
    from _config import config_server
    from dl.database import db

    # Register the app in the database
    db.init_app(app)

    #_ Run the application
    app.run(host=config_server.host, port=config_server.port)


if __name__ == '__main__':
    run()
