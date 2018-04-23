from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# The flask application
app = Flask("__name__")
Bootstrap(app)

# Setup the config from file
app.config.from_pyfile("config/config_app.py")

# Setup the DB (the comment below is a hack for Pycharm autocomplete)
db = SQLAlchemy(app)

# Setup the login manager and init
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Import the render views after setting up the application
from views import *


if __name__ == '__main__':
    from config.config_host import host, port
    app.run(host=host, port=port)
