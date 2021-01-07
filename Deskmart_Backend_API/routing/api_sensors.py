from flask import Blueprint, Response, request, abort, jsonify
from flask_cors import cross_origin

from controllers.influxdb_controller import InfluxController

sensor_blueprint = Blueprint("sensor", __name__)

db = InfluxController()

@sensor_blueprint.route("/", methods=["GET"])
def echo():
    return ("Sensor module")

@sensor_blueprint.route("/all", methods=["GET"])
@cross_origin()
def get_all_sensors():
    return jsonify(db.get_influx_data("username")), 200

@sensor_blueprint.route("/last", methods=["GET"])
@cross_origin()
def get_last_upload():
    return jsonify(db.get_last_timestamp("username")), 200

@sensor_blueprint.route("/last/flame", methods=["GET"])
@cross_origin()
def get_last_flame():
    return jsonify(db.get_last_flame("username")), 200

@sensor_blueprint.route("/last/humidity", methods=["GET"])
@cross_origin()
def get_last_humidity():
    return jsonify(db.get_last_hum("username")), 200

@sensor_blueprint.route("/last/temperature", methods=["GET"])
@cross_origin()
def get_last_temperature():
    return jsonify(db.get_last_temp("username")), 200

@sensor_blueprint.route("/heatmap/value", methods=["GET"])
@cross_origin()
def get_heatmap_value():
    return jsonify(db.get_capacitors_heatmap("username")), 200

@sensor_blueprint.route("/heatmap/color", methods=["GET"])
@cross_origin()
def get_heatmap_color():
    return jsonify(db.get_heatmap_colors("username")), 200

