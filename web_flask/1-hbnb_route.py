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
    """ Dsiplays hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, port='5000', host='0.0.0.0')
