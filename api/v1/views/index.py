#!/usr/bin/python3
"""
Index module for API status
it returns the status and stats
"""


from . import app_views
from models.amenity import Amenity
from models.city import City
from flask import jsonify
from models import storage
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review


@app_views.route('/status', strict_slashes=False, methods=['GET'])
def status():
    """ This return the status Ok"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False, methods=['GET'])
def count():
    """ Retrieve number of objects"""
    return jsonify({
            "amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)
        })


if __name__ == "__main__":
    pass
