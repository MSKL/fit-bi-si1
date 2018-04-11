from flask import request, render_template
from main import app, db
from models import Member


@app.route('/', methods=['GET'])
def index():
    name = request.values.get("name")
    email = request.values.get("mail")

    if name and email:
        # Create a new member
        new_member = Member(name=name, email=email)
        # Add it to the database session
        db.session.add(new_member)
        # Commit the change to the DB
        db.session.commit()

    # Get all members from the DB
    members = Member.query.all()

    # Render the template
    return render_template("index.html", title='Index - Members', members=members)