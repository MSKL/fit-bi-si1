"""
Top level module responsible for creating the application.
"""

from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from dl.MemberController import MemberController
from dl.RaceController import RaceController
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
member_controller = MemberController(db)                #: DB member controller
race_controller = RaceController(db)                    #: DB race controller

from pl.views import *


@login_manager.user_loader
def load_user(user_id):
    """
    Should take the unicode ID of a user, and return the corresponding user object.
    This function if required by the flask_login. Should not be removed.

    :type user_id: int
    :param user_id:
    """

    from dl.models.Member import Member
    return Member.query.get(user_id)


def register_views(_app):
    """
    Register all views to the application

    :param _app: flask application
    """

    _app.add_url_rule('/', view_func=IndexView.as_view('index'), methods=['GET'])
    _app.add_url_rule('/login/', view_func=LoginView.as_view('login'), methods=['GET', 'POST'])
    _app.add_url_rule('/logout', view_func=LogoutView.as_view('logout'), methods=['GET'])
    _app.add_url_rule('/admin_member', view_func=MemberAdminView.as_view('admin_member'), methods=['GET'])
    _app.add_url_rule('/profile/<user_id>', view_func=ProfileView.as_view('profile'))
    _app.add_url_rule('/admin_race', view_func=RaceAdminView.as_view('admin_race'), methods=['GET'])
    _app.add_url_rule('/race_detail/<race_id>', view_func=RaceDetailView.as_view('race_detail'), methods=['GET'])
    _app.add_url_rule('/race_edit/<race_id>', view_func=RaceEditView.as_view('race_edit'), methods=['GET'])


def run_app():
    """Run the application"""

    # Import the config and db
    from _config import config_server
    from dl.database import db

    # Register the app in the database
    db.init_app(app)

    # Register the views into the app
    try:
        register_views(app)
    except Exception as ex:
        print(str(ex))

    # Run the application
    app.run(host=config_server.host, port=config_server.port)
