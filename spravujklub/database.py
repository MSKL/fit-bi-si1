from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

if __name__ == "__main__":
    # TODO: Fix this
    db.create_all()