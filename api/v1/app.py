#!/usr/bin/python3

""" Flask Api module entry file"""


from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def tear_down(exception=None):
    """ Closes the database session on each request"""
    storage.close()


if __name__ == "__main__":
    import os
    host = os.environ.get("HBNB_API_HOST")
    port = os.environ.get("HBNB_API_PORT")
    app.run(port=port, host=host, threaded=True)