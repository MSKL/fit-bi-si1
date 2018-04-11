from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# The flask application
app = Flask("__name__")

# Setup the config from file
app.config.from_pyfile("config.py")

# Setup the DB
db = SQLAlchemy(app)

# Import the render views
from views import *

if __name__ == '__main__':
    app.run()