from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from dl.database import db


if __name__ == '__main__':
    """Run the application"""

    # The flask application
    app = Flask("__name__", template_folder="pl/templates")
    Bootstrap(app)

    # Setup the _config from file
    app.config.from_pyfile("../spravujklub/_config/config_app.py")

    # Setup the login manager and init
    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    # Setup the DB controllers
    from dl.MemberController import MemberController
    from dl.RaceController import RaceController

    member_controller = MemberController(db)
    race_controller = RaceController(db)

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

    # Import the config and db
    from _config import config_server
    from dl.database import db

    # Register the app in the database
    db.init_app(app)

    # Run the application
    app.run(host=config_server.host, port=config_server.port)
