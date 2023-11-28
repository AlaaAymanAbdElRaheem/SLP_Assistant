#!/usr/bin/python3
""" api/v1/views/age_range_id.py - handles RESTful API actions for age_range_id """

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage


# @app_views.route('/age_range_id/<age_from>', methods=['GET'], strict_slashes=False)
# def age_range_id(age_from):
#     """ Retrieves an age range by age_from """
#     age_range = storage.get_age_range_id(age_from)
#     if age_range is None:
#         abort(404)
#     return jsonify({'age_range_id':age_range})
