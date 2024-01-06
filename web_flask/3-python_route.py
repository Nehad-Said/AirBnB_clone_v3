#!/usr/bin/python3

"""
    Hello route
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """ Hello world"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello(text):
    """ With a parameter"""
    formatted = text.replace('_', ' ')
    return f"C {formatted}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytext(text="is cool"):
    """ With param and default"""
    formatted = text.replace('_', ' ')
    return f"Python {formatted}"


if __name__ == "__main__":
    app.run(debug=True, port='5000', host='0.0.0.0')
