#!/usr/bin/python3
""" RESTFul API - State """

from api.v1.views import app_views
from flask import Flask
from models import storage
from models.user import User
from flask import jsonify, request, abort


@app_views.route('/users/', methods=['GET'], strict_slashes=False)
def retrieve_list_all_users():
    """ Retrieves the list of all Amenity objects: GET /api/v1/amenities """
    if request.method == 'GET':
        list_all_storage = []
        for us in storage.all(User).values():
            list_all_storage.append(us.to_dict())
        return jsonify(list_all_storage)
