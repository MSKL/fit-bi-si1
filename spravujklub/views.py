from flask import request, render_template

from entities.Race import Race
from entities.User import User
from main import app, db
from models import Member
import datetime


@app.route('/', methods=['GET'])
def index():
    name = request.values.get("name")
    email = request.values.get("mail")
    delete = request.values.get("delete")

    if name and email:
        # Create a new member
        new_member = Member(name=name, email=email)
        # Add it to the database session
        db.session.add(new_member)
        # Commit the change to the DB
        db.session.commit()

    if delete:
        memb = db.session.query(Member).get(delete)
        db.session.delete(memb)
        db.session.commit()

    # Get all members from the DB
    members = Member.query.all()

    # Render the template
    return render_template("index.html", members=members, title="SpravujKlub", user=User("Lukas", "test@test.cz"))

@app.route('/races', methods=['GET'])
def races():
    races = []
    races.append(Race("Zavod1", "Zavodovice", datetime.date(2018, 1,8), True))
    races.append(Race("Zavod2", "testtest", datetime.date(2018, 1,8), False))
    races.append(Race("Zavod3", "Racetown", datetime.date(2018, 1,8), False))
    races.append(Race("Zavod4", "Zavodnikov", datetime.date(2018, 1,8), True))
    # Render the template
    return render_template("races.html", races=races, user=User("Lukas", "test@test.cz"))

@app.route('/profile', methods=[ 'GET' ])
def profile():
        # TODO
        # Render the template
        return render_template("profile.html", user=User("Lukas", "test@test.cz"))
