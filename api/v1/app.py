#!/usr/bin/python3
""" Flask app """

from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


# @app.teardown_appcontext
# def teardown_appcontext(self):
#     """ Closes the storage """
#     storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ 404 page not found """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = getenv("SLP_API_HOST", default="0.0.0.0")
    port = getenv("SLP_API_PORT", default="5000")
    app.run(host=host, port=port, threaded=True)
