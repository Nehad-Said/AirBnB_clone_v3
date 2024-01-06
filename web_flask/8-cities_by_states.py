#!/usr/bin/python3

"""
    HBNB Route that displays a list of states
"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_states():
    """ Displays a list of cities with their states"""
    states = list(storage.all(State).values())
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_req(exception=None):
    """ Closes the session after the request """
    storage.close()


if __name__ == "__main__":
    app.run(port='5000', host='0.0.0.0')
