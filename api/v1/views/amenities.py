#!/usr/bin/python3
""" RESTFul API - State """

from api.v1.views import app_views
from flask import Flask
from models import storage
from models.amenity import Amenity
from flask import jsonify, request, abort


@app_views.route('/amenities/', methods=['GET'], strict_slashes=False)
def retrieve_list_all_amenities():
    """ Retrieves the list of all Amenity objects: GET /api/v1/amenities """
    if request.method == 'GET':
        list_all_storage = []
        for am in storage.all(Amenity).values():
            list_all_storage.append(am.to_dict())
        return jsonify(list_all_storage)
