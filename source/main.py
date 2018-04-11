from flask import Flask, render_template


# The flask application
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
        return render_template("index.html", title='Hello world')


if __name__ == '__main__':
    app.run(debug=True)
