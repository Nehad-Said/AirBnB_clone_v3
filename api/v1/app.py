#!/usr/bin/python3
"""
Module
Flask Api module entry file (app).
This is the main file of AirBnB project APIs

"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(exception=None):
    """ Closes the database session on each request"""
    storage.close()


@app.errorhandler(404)
def handle_error(e):
    """ Return a json error"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST")
    port = int(os.environ.get("HBNB_API_PORT"))
    if port is None:
        port = 5000
    if host is None:
        host = "0.0.0.0"
    app.run(port=port, host=host, threaded=True)
