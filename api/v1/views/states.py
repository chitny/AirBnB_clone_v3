#!/usr/bin/python3
""" RESTFul API - State """

from api.v1.views import app_views
from flask import Flask
from models import storage
from models.state import State
from flask import jsonify, request, abort


@app_views.route('/states/', methods=['GET'])
def retrieve_list_all_states():
    """ Retrieves the list of all State objects: GET /api/v1/states """
    if request.method == 'GET':
        list_all_storage = []
        for st in storage.all(State).values():
            list_all_storage.append(st.to_dict())
        return jsonify(list_all_storage)


@app_views.route('/states/<state_id>', methods=['GET'])
def retrieve_one_state(state_id):
    """ Retrieves a State object: GET /api/v1/states/<state_id> """
    if request.method == 'GET':
        if storage.get(State, state_id) is not None:
            return jsonify(storage.get(State, state_id).to_dict())
        abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_one_state(state_id):
    """ Deletes a State object:: DELETE /api/v1/states/<state_id> """
    if request.method == 'DELETE':
        if storage.get(State, state_id) is not None:
            # antes de eliminar un State, hay que eliminar sus cities
            storage.delete(storage.get(State, state_id))
            storage.save()
            return {}, 200
        abort(404)


@app_views.route('/states/', methods=['POST'])
def create_new_state(state_id):
    """ Creates a State: POST /api/v1/states """
