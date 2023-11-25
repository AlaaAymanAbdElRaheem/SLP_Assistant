#!/usr/bin/python3
""" Flask app """


from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


if app_views is not None:
    from api.v1.views.milestones import *
    from api.v1.views.age_range_id import *
