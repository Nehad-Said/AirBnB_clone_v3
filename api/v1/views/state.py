#!/usr/bin/python3
""" State api module """

from models import storage
from models.state import State
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/states', strict_slashes=False, methods=['GET'])
def get_all_states():
    """ Returns the list of all states"""
    all_states = storage.all(State)
    my_states = []
    for key, value in all_states.items():
        my_states.append(value.to_dict())
    return jsonify(my_states)


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['GET'])
def get_state(state_id):
    """ Retrieves a single state"""
    all_states = storage.all(State)
    my_states = []
    for key, value in all_states.items():
        my_states.append(value.to_dict())
    for state in my_states:
        if state['id'] == state_id:
            return jsonify(state)
    return abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def del_state(state_id):
    """ Retrieves a single state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    try:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    except KeyError:
        abort(404)


@app_views.route('/states', strict_slashes=False, methods=['POST'])
def add_state():
    """ Add a new state"""
    name = request.get_json().get("name")
    if request.content_type != "application/json":
        abort(400)
    if name is None:
        abort(400)
    new_state = State(name=name)
    storage.new(new_state)
    storage.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['PUT'])
def update_state(state_id):
    """ Update a given state """
    data = request.get_json()
    if request.content_type != "application/json":
        abort(400)
    if data is None:
        abort(400)
    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    for key, value in data.items():
        if key != 'id' and key != 'created_at' and key != 'updated_at':
            setattr(state, key, value)

    storage.save()
    return jsonify(state.to_dict()), 200
