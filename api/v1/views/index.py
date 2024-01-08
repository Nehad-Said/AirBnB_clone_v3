#!/usr/bin/python3

""" Index Blue print file"""


from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """ This return the status Ok"""
    return jsonify({"status": "OK"})
