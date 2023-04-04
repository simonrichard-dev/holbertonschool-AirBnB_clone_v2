#!/usr/bin/python3
""" Comment """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello0():
    """ function that return Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello1():
    """ function that return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello2(text):
    """ function that return C then a text variable"""
    return f"C {escape(text)}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
