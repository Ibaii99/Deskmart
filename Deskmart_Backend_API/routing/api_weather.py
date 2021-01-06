from flask import Blueprint, Response, request, abort, jsonify
from flask_cors import cross_origin

weather_blueprint = Blueprint("weather", __name__)

@weather_blueprint.route("/", methods=["GET"])
def echo():
    return ("Weahter module")