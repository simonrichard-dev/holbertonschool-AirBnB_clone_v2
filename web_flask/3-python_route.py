#!/usr/bin/python3
""" A script that starts a Flask web application """
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
    text = text.replace("_", " ")
    text = "C {}".format(text)
    return text


@app.route("/c/<text>", strict_slashes=False)
def hello3(text):
    """ function that return C then a text variable"""
    if text is None:
        text = "is cool"
    else:
        text = text.replace("_", " ")
        text = "C {}".format(text)
    return text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello4(text='is cool'):
    """ function that return Python then a text variable"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
