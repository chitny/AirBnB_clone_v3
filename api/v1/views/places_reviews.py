#!/usr/bin/python3
""" RESTFul Api - City """

from api.v1.views import app_views
from flask import Flask
from models import storage
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from flask import jsonify, request, abort


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def reviews_by_place_id(place_id):
    """ Retrieves the list of all Review objects of a Place """
    if request.method == 'GET':
        if storage.get(Place, place_id) is not None:
            reviews = []
            for re in storage.all(Review).values():
                if re.place_id == place_id:
                    reviews.append(re.to_dict())
            return jsonify(reviews)
        abort(404)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def retrieve_one_review(review_id):
    """ Retrieves a Review object. : GET /api/v1/reviews/<review_id> """
    if request.method == 'GET':
        if storage.get(Review, review_id) is not None:
            return jsonify(storage.get(Review, review_id).to_dict())
        abort(404)


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_one_review(review_id):
    """ Deletes a Review object: DELETE /api/v1/reviews/<review_id> """
    if request.method == 'DELETE':
        if storage.get(Review, review_id) is not None:
            storage.delete(storage.get(Review, review_id))
            storage.save()
            return jsonify({}), 200
        abort(404)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_new_review(review_id):
    """ Creates a Review: POST /api/v1/places/<place_id>/reviews """
    if request.method == 'POST':
        if storage.get(Place, place_id) is not None:
            req_type = request.headers.get('Content-Type')
            if req_type != 'application/json':
                return jsonify('Not a JSON'), 400
            dict_req = request.get_json()
            if 'user_id' not in dict_req:
                return jsonify('Missing user_id'), 400
            if storage.get(User, dict_req['user_id']) is None:
                abort(404)
            else:
                if 'text' not in dict_req:
                    return jsonify('Missing text'), 400
                new_obj_Review = Review(**dict_req)
                new_obj_Review.user_id = dict_req['user_id']
                new_obj_Review.place_id = place_id
                new_obj_Review.save()
                return jsonify(new_obj_Review.to_dict()), 201
        abort(404)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """ Updates a Review object: PUT /api/v1/reviews/<review_id> """
    if request.method == 'PUT':
        review = storage.get(Review, review_id)
        if not review:
            abort(404)
        req_type = request.headers.get('Content-Type')
        if req_type != 'application/json':
            return jsonify('Not a JSON'), 400
        dict_req = request.get_json()
        try:
            review.text = dict_req['text']
            storage.save()
        except Exception as e:
            print(e)
        return jsonify(review.to_dict()), 200
