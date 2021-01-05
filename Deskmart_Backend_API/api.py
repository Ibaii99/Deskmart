from flask import Flask, Blueprint, abort, request, Response, jsonify
from flask_cors import CORS, cross_origin
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import json
from routing import api_users
import config
import logging
import sys
sys.path.append('../')
sys.path.append('../Deskmart_Backend_Logic')
sys.path.append('../Deskmart_Frontend')
from logic.authorization import Authorization
from Deskmart_Backend_Logic import rp


app = Flask(__name__)
#app.register_blueprint(api_markets.markets_blueprint, url_prefix=config.API_URL_PREFIX+"/market")
app.register_blueprint(api_users.users_blueprint, url_prefix=config.API_URL_PREFIX + "/user")

cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['CORS_HEADERS'] = ['Content-Type', 'Authorization']

org = "jorge.elbusto@opendeusto.es"
bucket = "DeskMart"

client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=config.INFLUXDB_TOKEN)

def sequencify(username, hum, temp, hayLlama, cap11, cap12, cap21, cap22):
    sequence = ["humTemp,usuario=" + username + " humedad=" + hum,
                "humTemp,usuario=" + username + " temperatura=" + temp,
                "llama,usuario=" + username + " hayLlama=" + hayLlama,
                "Capacitors,usuario=" + username + " cap11=" + cap11,
                "Capacitors,usuario=" + username + " cap12=" + cap12,
                "Capacitors,usuario=" + username + " cap21=" + cap21,
                "Capacitors,usuario=" + username + " cap22=" + cap22]
    return sequence

'''
a este metodo se le pasa el resultado del sequencify, podriamos combinarlo en uno que pase
las variables y escriba en la api directamente
'''
def writeOnInflux(sequence):
    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket, org, sequence)

def getInfluxData():
    query = 'from(bucket: "DeskMart") |> range(start: -12h, stop: now()) |> filter(fn: (r) => r["_measurement"] == "Capacitors" or r["_measurement"] == "humTemp" or r["_measurement"] == "llama")' #FALLA LA QUERY


    result = client.query_api().query(query, org=org)

    results = []
    for table in result:
        for record in table.records:
            results.append((record.get_time().strftime("%m/%d/%Y, %H:%M:%S"), record.get_field(), record.get_value()))

    results_ordenados = sorted(results, key=lambda tup: tup[0])

    for x in results_ordenados:
        print(x)

    return results_ordenados

@app.route('/', methods=["GET"])
@cross_origin()
def hello():
    return "Hello World!"

@app.before_request
def check_api_key():
    if request.method == 'OPTIONS':
        resp = app.make_default_options_response()

        headers = None
        if 'ACCESS_CONTROL_REQUEST_HEADERS' in request.headers:
            headers = request.headers['ACCESS_CONTROL_REQUEST_HEADERS']

        h = resp.headers

        # Allow the origin which made the XHR
        h['Access-Control-Allow-Origin'] = request.headers['Origin']
        # Allow the actual method
        h['Access-Control-Allow-Methods'] = request.headers['Access-Control-Request-Method']
        # Allow for 10 seconds
        h['Access-Control-Max-Age'] = "10"

        # We also keep current headers
        if headers is not None:
            h['Access-Control-Allow-Headers'] = headers
        
        return resp
    else:
        logging.warning("BEFORE")
        # logging.warning(request.headers)
        api_key = request.headers.get("X-Api-Key")
        try:
            auth = request.headers.get("Authorization")
        except:
            auth = None
        if (api_key is not None and auth is not None):
            if not Authorization.authorize_user_token(request) or not Authorization.authorize_front(api_key):  
                abort(401)
            else:
                pass
        elif (api_key is not None and auth is None):
            if not Authorization.authorize_front(api_key) and is_get_token_route(request.url_rule):
                abort(401)
            else: 
                pass
        else:
            abort(403)

@app.after_request
def save_history(response):
    logging.warning("After")

    # logging.warning(response)
    # logging.warning(request)
    # logging.warning(request.headers)
    # logging.warning(request.cookies)
    # logging.warning(request.args)
    # logging.warning(request.url_rule)   
    return response

def is_get_token_route(route):
    login_route= "/api/v1/user/login"
    register_route= "/api/v1/user/register"
    if route == login_route or route == register_route:
        return True
    else:
        return False


@app.errorhandler(403)
def page_not_found(e):
    return jsonify(json.dumps("Forbbiden access, invalid api-key")), 403

@app.errorhandler(401)
def page_not_found(e):
    return jsonify(json.dumps("Incorrect username or password")), 401

if __name__ == '__main__':
    getInfluxData()
    '''valSensores = rp.getSensors() #[flameValue, touchValue, humValue, tempValue]
    flame = str(valSensores[0]) #casteamos sensores a string
    touch = str(valSensores[1])
    hum = str(valSensores[2])
    temp = str(valSensores[3])
    sequence = sequencify("current_user",hum,temp,flame,touch,touch,touch,touch) #aquí habría que poner los capacitores
    print(sequence)
    writeOnInflux(sequence)'''


    #app.run(debug=True, host=config.HOST, port=config.PORT)


