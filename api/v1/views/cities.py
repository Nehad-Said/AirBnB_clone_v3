#!/usr/bin/python3
""" State api module """

from models import storage
from models.city import City
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/cities', strict_slashes=False, methods=['GET'])
def get_all_city():
    """ Returns the list of all city"""
    all_cities = storage.all(City)
    my_cities = []
    for key, value in all_cities.items():
        my_cities.append(value.to_dict())
    return jsonify(my_cities)


@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['GET'])
def get_city(city_id):
    """ Retrieves a single city"""
    all_cities = storage.all(City)
    my_cities = []
    for key, value in all_cities.items():
        my_cities.append(value.to_dict())
    for city in my_cities:
        if city['id'] == city_id:
            return jsonify(city)
    return abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def del_city(city_id):
    """ Retrieves a single state"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    try:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    except KeyError:
        abort(404)


@app_views.route('/cities', strict_slashes=False, methods=['POST'])
def add_city():
    """ Add a new city"""
    name = request.get_json().get("name")
    if request.content_type != "application/json":
        abort(400)
    if name is None:
        abort(400)
    new_city = City(name=name)
    storage.new(new_city)
    storage.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['PUT'])
def update_city(city_id):
    """ Update a given city """
    data = request.get_json()
    if request.content_type != "application/json":
        abort(400)
    if data is None:
        abort(400)
    city = storage.get(City, city_id)

    if city is None:
        abort(404)

    for key, value in data.items():
        if key != 'id' and key != 'created_at' and key != 'updated_at':
            setattr(city, key, value)

    storage.save()
    return jsonify(city.to_dict()), 200
