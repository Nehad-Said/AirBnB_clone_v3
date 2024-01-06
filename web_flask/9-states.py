#!/usr/bin/python3

"""
    HBNB Route that displays a list of states
"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_with_id(id=None):
    """ Display single state"""
    states = sorted(list(storage.all(State).values()),
                    key=lambda s: s.name)
    if id:
        for state in states:
            if state.id == id:
                found_state = state
        return render_template('9-states.html', states=state, found_state=found_state)
    else:
        return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown_req(exception=None):
    """ Closes the session after the request """
    storage.close()


if __name__ == "__main__":
    app.run(port='5000', host='0.0.0.0')
