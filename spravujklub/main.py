from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# The flask application
app = Flask("__name__")
Bootstrap(app)

# Setup the config from file
app.config.from_pyfile("config.py")

# Setup the DB (the comment below is a hack for Pycharm autocomplete)
db = SQLAlchemy(app)
""":type: sqlalchemy.orm.SQLAlchemy"""

# Setup the login manager and init
login_manager = LoginManager()
login_manager.init_app(app)

# Import the render views
from views import *


@login_manager.user_loader
def load_user(user_id):
    """should take the unicode ID of a user, and return the corresponding user object"""
    return User.get(user_id)


if __name__ == '__main__':
    """run the application"""
    app.run()
