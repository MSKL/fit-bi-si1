from flask import render_template
from main import app
from models import Member

@app.route('/')
def index():
    first_member = Member.query.first()
    example_content = "First member's name is " + first_member.name + "."
    return render_template("index.html", title='Hello world', content=example_content)