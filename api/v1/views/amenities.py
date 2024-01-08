#!/usr/bin/python3
""" State api module """

from models import storage
from models.amenities import Amenity
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/amenities', strict_slashes=False, methods=['GET'])
def get_all_amenities():
    """ Returns the list of all amenities"""
    all_amenities = storage.all(Amenity)
    my_amenities = []
    for key, value in all_amenities.items():
        my_amenities.append(value.to_dict())
    return jsonify(my_amenities)


@app_views.route('/amenities/<amenity_id>', strict_slashes=False, methods=['GET'])
def get_amenity(amenity_id):
    """ Retrieves a single Amenity"""
    all_amenities = storage.all(Amenity)
    my_amenities = []
    for key, value in all_amenities.items():
        my_amenities.append(value.to_dict())
    for amenity in my_amenities:
        if amenity['id'] == amenity_id:
            return jsonify(amenity)
    return abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def del_amenity(amenity_id):
    """ Retrieves a single amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    try:
        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200
    except KeyError:
        abort(404)


@app_views.route('/amenities', strict_slashes=False, methods=['POST'])
def add_amenity():
    """ Add a new amenity"""
    name = request.get_json().get("name")
    if request.content_type != "application/json":
        abort(400)
    if name is None:
        abort(400)
    new_amenity = Amenity(name=name)
    storage.new(new_amenity)
    storage.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', strict_slashes=False, methods=['PUT'])
def update_amenity(amenity_id):
    """ Update a given amenity """
    data = request.get_json()
    if request.content_type != "application/json":
        abort(400)
    if data is None:
        abort(400)
    amenity = storage.get(Amenity, amenity_id)

    if amenity is None:
        abort(404)

    for key, value in data.items():
        if key != 'id' and key != 'created_at' and key != 'updated_at':
            setattr(amenity, key, value)

    storage.save()
    return jsonify(amenity.to_dict()), 200
