#!/usr/bin/python3
"""Module containing the flask app and the error handlers"""

from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def teardown_appcontext(self):
    """ Closes the storage """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ 404 page not found """
    return make_response(jsonify({"error": "Not found"}), 404)


@app.errorhandler(500)
def handle_500(error):
    """ 500 internal server error """
    original = getattr(error, "original_exception", None)

    if original is None:
        """ direct 500 error, such as abort(500)"""
        return make_response(jsonify({"error": "Internal Server Error"}), 500)

    """wrapped unhandled error"""
    return make_response(jsonify(
        {"error": "Internal Server Error: " + str(original)}), 500)


if __name__ == "__main__":
    host = getenv("SLP_API_HOST", default="0.0.0.0")
    port = getenv("SLP_API_PORT", default="5000")
    app.run(host=host, port=port, threaded=True)
