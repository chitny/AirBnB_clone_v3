#!/usr/bin/python3
""" RESTFul Api - City """

from api.v1.views import app_views
from flask import Flask
from models import storage
from models.city import City
from models.state import State
from flask import jsonify, request, abort


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def cities_by_state_id(state_id):
    """ Retrieves the list of all City objects of a State: GET /api/v1/states/<state_id>/cities """
    if storage.get(State, state_id) is not None:
        li_cities = storage.all(City).values()
        for ci in li_cities:
            ci.to_dict()
        return jsonify(li_cities)
    abort(404)
"""
@app_views.route('/states/', methods=['GET'])
def retrieve_list_all_states():
    if request.method == 'GET':
        list_all_storage = []
        for st in storage.all(State).values():
            list_all_storage.append(st.to_dict())
        return jsonify(list_all_storage)
"""
