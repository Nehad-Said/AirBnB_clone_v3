#!/usr/bin/python3
"""Flask module for AirBnB APIs"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def tear_down(exception):
    """closes the database after a req"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """handle error"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)
