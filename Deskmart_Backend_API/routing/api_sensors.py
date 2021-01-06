from flask import Blueprint, Response, request, abort, jsonify
from flask_cors import cross_origin

from controllers.influxdb_controller import InfluxController

sensor_blueprint = Blueprint("sensor", __name__)


@sensor_blueprint.route("/", methods=["GET"])
def echo():
    return ("Sensor module")

@sensor_blueprint.route("/all", methods=["GET"])
@cross_origin()
def get_all_sensors():
    db = InfluxController()
    return jsonify(db.get_influx_data()), 200

#ESTÁN TODOS LOS MÉTODOS BIEN EN INFLUXDB_CONTROLLER
