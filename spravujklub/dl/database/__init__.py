"""
This module is responsible for creating the DB.
"""

from flask_sqlalchemy import SQLAlchemy

#: The database engine is set here
db = SQLAlchemy()