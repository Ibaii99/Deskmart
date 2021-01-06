from flask import Blueprint, Response, request, abort, jsonify
from flask_cors import cross_origin
import pyowm
import config

weather_blueprint = Blueprint("weather", __name__)

@weather_blueprint.route("/", methods=["GET"])
def echo():

    owm = pyowm.OWM(config.OWM_APIKEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Bilbao, ES')
    w = observation.weather
    temp = w.temperature('celsius')
    tiempo = {
        "temperatura": temp['temp'],
        "max": temp['temp_max'],
        "min": temp['temp_min']
    }
    return jsonify(tiempo), 200