from logging import debug
from flask import Flask, redirect, url_for
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)