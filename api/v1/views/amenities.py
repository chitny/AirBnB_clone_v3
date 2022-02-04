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


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def retrieve_one_amenity(amenity_id):
    """ Retrieves a Amenity object: GET /api/v1/states/<state_id> """
    if request.method == 'GET':
        if storage.get(Amenity, amenity_id) is not None:
            return jsonify(storage.get(Amenity, amenity_id).to_dict())
        abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_one_amenity(amenity_id):
    """ Deletes a State object:: DELETE /api/v1/states/<state_id> """
    if request.method == 'DELETE':
        if storage.get(Amenity, amenity_id) is not None:
            storage.delete(storage.get(Amenity, amenity_id))
            storage.save()
            return jsonify({}), 200
        abort(404)
