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
    one_call = mgr.one_call(lat=43.26166, lon=-2.9393129)
    tiempo = {
        "temperatura": temp['temp'],
        "max": temp['temp_max'],
        "min": temp['temp_min'],
        "tiempo": w.detailed_status,
        "humedad": w.humidity,
        "icono": one_call.forecast_daily[0].weather_icon_url()
    }
    return jsonify(tiempo), 200