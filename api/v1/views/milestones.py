#!/usr/bin/python3
""" api/v1/views/milestones.py - handles RESTful API actions for milestones """

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.child_milestone import ChildMilestone

@app_views.route('/milestones/<age_range_id>', methods=['GET'], strict_slashes=False)
def milestones_by_age_range(age_range_id):
    """ Retrieves all milestones for a given age range """
    milestones = storage.get_milestones(age_range_id)
    if milestones is None:
        abort(404)
    return jsonify([milestone.to_dict() for milestone in milestones])
