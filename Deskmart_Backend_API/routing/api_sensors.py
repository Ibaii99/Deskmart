from flask import Blueprint, Response, request, abort, jsonify
from flask_cors import cross_origin

from utils import COOKIE_MANAGER
import logging

from controllers.influxdb_controller import InfluxController
from controllers.users_controller import UsersController
from controllers.sessions_controller import SessionsController

sensor_blueprint = Blueprint("sensor", __name__)

db = InfluxController()

@sensor_blueprint.route("/", methods=["GET"])
def echo():
    return ("Sensor module")

@sensor_blueprint.route("/all", methods=["GET"])
@cross_origin()
def get_all_sensors():
    return jsonify(db.get_influx_data(get_user_name(request))), 200

@sensor_blueprint.route("/distinct", methods=["GET"])
@cross_origin()
def get_distinct_dates():
    return jsonify(db.get_distinct_days(get_user_name(request))), 200

@sensor_blueprint.route("/last", methods=["GET"])
@cross_origin()
def get_last_upload():
    return jsonify(db.get_last_timestamp(get_user_name(request))), 200

@sensor_blueprint.route("/last/flame", methods=["GET"])
@cross_origin()
def get_last_flame():
    return jsonify(db.get_last_flame(get_user_name(request))), 200

@sensor_blueprint.route("/last/humidity", methods=["GET"])
@cross_origin()
def get_last_humidity():
    return jsonify(db.get_last_hum(get_user_name(request))), 200

@sensor_blueprint.route("/last/temperature", methods=["GET"])
@cross_origin()
def get_last_temperature():
    return jsonify(db.get_last_temp(get_user_name(request))), 200

@sensor_blueprint.route("/heatmap/value", methods=["GET"])
@cross_origin()
def get_heatmap_value():
    year = request.headers.get('year')
    month = request.headers.get('month')
    day = request.headers.get('day')
    return jsonify(db.get_capacitors_heatmap(get_user_name(request), day, month, year)), 200

@sensor_blueprint.route("/heatmap/color", methods=["GET"])
@cross_origin()
def get_heatmap_color():
    year = request.headers.get('year')
    month = request.headers.get('month')
    day = request.headers.get('day')
    return jsonify(db.get_heatmap_colors(get_user_name(request), day, month, year)), 200


@sensor_blueprint.route("/heatmap/touches", methods=["GET"])
@cross_origin()
def get_heatmap_touches():
    year = request.headers.get('year')
    month = request.headers.get('month')
    day = request.headers.get('day')
    return jsonify(db.get_capacitors_touch_time(get_user_name(request), day, month, year)), 200

users_db = UsersController()
sessions_db = SessionsController()

def get_user_name(request):
    session_cookie = COOKIE_MANAGER.get_authorization_token_decoded(request)
    if session_cookie:
        session = sessions_db.get(session_cookie)
        if session:
            user = users_db.get(session_cookie.get("username"))
            if user:
                if user.email:
                    return user.email
                    
    abort(401)
