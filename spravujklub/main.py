from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from dl.MemberController import MemberController
from dl.RaceController import RaceController
from database import db

# The flask application
app = Flask("__name__", template_folder="pl/templates")
Bootstrap(app)

# Setup the _config from file
app.config.from_pyfile("_config/config_app.py")

# Setup the login manager and init
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Setup the DB controllers
member_controller = MemberController(db)
race_controller = RaceController(db)


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
    from pl.views.index import *
    from pl.views.login import *
    from pl.views.logout import *
    from pl.views.profile import *
    from pl.views.admin_member import *
    from pl.views.admin_race import *
    from pl.views.race_detail import *
    from pl.views.race_edit import *

    # Import the config and db
    from _config import config_server
    from database import db

    # Register the app in the database
    db.init_app(app)

    # Run the application
    app.run(host=config_server.host, port=config_server.port)
