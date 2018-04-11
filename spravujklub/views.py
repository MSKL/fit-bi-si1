from flask import request, render_template
from main import app, db
from models import Member


@app.route('/', methods=['GET'])
def index():
    name = request.values.get("name")
    email = request.values.get("mail")

    if name and email:
        print("Adding: " + name + " mail: " + email)
        new_member = Member(name=name, email=email)
        db.session.add(new_member)
        db.session.commit()

    members = Member.query.all()
    return render_template("index.html", title='Hello world', members=members)