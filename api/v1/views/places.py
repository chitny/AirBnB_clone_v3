#!/usr/bin/python3
""" RESTFul Api - City """

from api.v1.views import app_views
from flask import Flask
from models import storage
from models.city import City
from models.user import User
from models.place import Place
from flask import jsonify, request, abort


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def places_by_city_id(city_id):
    """ Retrieves the list of all Place objects of a City """
    if request.method == 'GET':
        if storage.get(City, city_id) is not None:
            places = []
            for pl in storage.all(Place).values():
                if pl.city_id == city_id:
                    places.append(pl.to_dict())
            return jsonify(places)
        abort(404)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def retrieve_one_place(place_id):
    """ Retrieves a Place object. : GET /api/v1/places/<place_id> """
    if request.method == 'GET':
        if storage.get(Place, place_id) is not None:
            return jsonify(storage.get(Place, place_id).to_dict())
        abort(404)


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_one_place(place_id):
    """ Deletes a Place object: DELETE /api/v1/places/<place_id> """
    if request.method == 'DELETE':
        if storage.get(Place, place_id) is not None:
            storage.delete(storage.get(Place, place_id))
            storage.save()
            return jsonify({}), 200
        abort(404)
