from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# The flask application
app = Flask("__name__")
Bootstrap(app)

# Setup the config from file
app.config.from_pyfile("config.py")

# Setup the DB (the comment below is a hack for Pycharm autocomplete)
db = SQLAlchemy(app)
""":type: sqlalchemy.orm.SQLAlchemy"""

# Import the render views
from views import *

if __name__ == '__main__':
    app.run()
