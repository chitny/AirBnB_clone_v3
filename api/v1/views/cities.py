#!/usr/bin/python3
""" RESTFul Api - City """

from api.v1.views import app_views
from flask import Flask
from models import storage
from models.city import City
from models.state import State
from flask import jsonify, request, abort


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def cities_by_state_id(state_id):
    """ Retrieves the list of all City objects of a State """
    if request.method == 'GET':
        if storage.get(State, state_id) is not None:
            cities = []
            for ci in storage.all(City).values():
                if ci.state_id == state_id:
                    cities.append(ci.to_dict())
            return jsonify(cities)
        abort(404)
