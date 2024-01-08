#!/usr/bin/python3

""" Index Blue print file"""


from api.v1.views import app_views


@app_views.route('/api/v1/status')
def status():
    """ This return the status Ok"""
    return {"status": "OK"}
