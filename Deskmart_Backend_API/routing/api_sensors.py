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
    return jsonify(db.get_influx_data("rp-jorge-ibai")), 200

@sensor_blueprint.route("/last", methods=["GET"])
@cross_origin()
def get_last_upload():
    return jsonify(db.get_last_timestamp("rp-jorge-ibai")), 200

@sensor_blueprint.route("/last/flame", methods=["GET"])
@cross_origin()
def get_last_flame():
    return jsonify(db.get_last_flame("rp-jorge-ibai")), 200

@sensor_blueprint.route("/last/humidity", methods=["GET"])
@cross_origin()
def get_last_humidity():
    return jsonify(db.get_last_hum("rp-jorge-ibai")), 200

@sensor_blueprint.route("/last/temperature", methods=["GET"])
@cross_origin()
def get_last_temperature():
    return jsonify(db.get_last_temp("rp-jorge-ibai")), 200

@sensor_blueprint.route("/heatmap/value", methods=["GET"])
@cross_origin()
def get_heatmap_value():
    return jsonify(db.get_capacitors_heatmap("rp-jorge-ibai")), 200

@sensor_blueprint.route("/heatmap/color", methods=["GET"])
@cross_origin()
def get_heatmap_color():
    return jsonify(db.get_heatmap_colors("rp-jorge-ibai")), 200

