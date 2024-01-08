#!/usr/bin/python3
""" State api module """

from models import storage
from models.user import User
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/users', strict_slashes=False, methods=['GET'])
def get_all_user():
    """ Returns the list of all users"""
    all_users = storage.all(User)
    my_users = []
    for key, value in all_users.items():
        my_users.append(value.to_dict())
    return jsonify(my_users)


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['GET'])
def get_user(user_id):
    """ Retrieves a single user"""
    all_users = storage.all(User)
    my_users = []
    for key, value in all_users.items():
        my_users.append(value.to_dict())
    for user in my_users:
        if user['id'] == user_id:
            return jsonify(user)
    return abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'])
def del_user(user_id):
    """ Retrieves a single user"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    try:
        storage.delete(user)
        storage.save()
        return jsonify({}), 200
    except KeyError:
        abort(404)


@app_views.route('/users', strict_slashes=False, methods=['POST'])
def add_user():
    """ Add a new user"""
    name = request.get_json().get("name")
    if request.content_type != "application/json":
        abort(400)
    if name is None:
        abort(400)
    new_user = User(name=name)
    storage.new(new_users)
    storage.save()
    return jsonify(new_users.to_dict()), 201


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['PUT'])
def update_user(user_id):
    """ Update a given user """
    data = request.get_json()
    if request.content_type != "application/json":
        abort(400)
    if data is None:
        abort(400)
    user = storage.get(User, user_id)

    if user is None:
        abort(404)

    for key, value in data.items():
        if key != 'id' and key != 'created_at' and key != 'updated_at':
            setattr(user, key, value)

    storage.save()
    return jsonify(users.to_dict()), 200
