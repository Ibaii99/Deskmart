from flask import Blueprint, Response, request, abort, jsonify
from flask_cors import cross_origin
import pyowm
import config
import json
from utils import COOKIE_MANAGER
from logic.authorization import Authorization
from controllers.users_controller import UsersController

from controllers.sessions_controller import SessionsController

weather_blueprint = Blueprint("weather", __name__)

users_db = UsersController()
sessions_db = SessionsController()

@weather_blueprint.route("/", methods=["GET"])
def echo():
    return "Weather module"


@weather_blueprint.route("/today", methods=["GET"])
@cross_origin()
def get_today_weather():
    session_cookie = COOKIE_MANAGER.get_authorization_token_decoded(request)
    if session_cookie:
        session = sessions_db.get(session_cookie)
        if session:
            user = users_db.get(session_cookie.get("username"))
            if user:
                if user.city:
                    owm = pyowm.OWM(config.OWM_APIKEY)
                    mgr = owm.weather_manager()
                    observation = mgr.weather_at_place('{}, ES'.format(user.city))
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
                else:
                    tiempo = {
                        "temperatura": 0,
                        "max": 0,
                        "min": 0,
                        "tiempo": 0,
                        "humedad": 0,
                        "icono": 0
                    }
                return jsonify(tiempo), 200
    abort(401)
    
    