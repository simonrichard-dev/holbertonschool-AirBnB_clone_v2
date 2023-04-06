#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_hello_hbnb():
    """ function that return Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """ function that return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def replace_(text):
    """ function that return C then a text variable"""
    text = text.replace("_", " ")
    text = "C {}".format(text)
    return text


@app.route("/c/<text>", strict_slashes=False)
def C_is_cool(text):
    """ function that return C then a text variable"""
    if text is None:
        text = "is cool"
    else:
        text = text.replace("_", " ")
        text = "C {}".format(text)
    return text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python_is_fun(text='is cool'):
    """ function that return Python then a text variable"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    """ function that display “n is a number” only if n is an integer """
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ function that display a HTML page if n is an integer """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """ function that display a HTML page if n is an integer
        & checks if it's odd or even """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
