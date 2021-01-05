from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import config


class InfluxController:
    def __init__(self):
        self.org = "jorge.elbusto@opendeusto.es"
        self.bucket = "DeskMart"
        self.client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=config.INFLUXDB_TOKEN)
        
    def sequencify(self, username, hum, temp, hayLlama, cap11, cap12, cap21, cap22):
        sequence = ["humTemp,usuario=" + username + " humedad=" + hum,
                    "humTemp,usuario=" + username + " temperatura=" + temp,
                    "llama,usuario=" + username + " hayLlama=" + hayLlama,
                    "Capacitors,usuario=" + username + " cap11=" + cap11,
                    "Capacitors,usuario=" + username + " cap12=" + cap12,
                    "Capacitors,usuario=" + username + " cap21=" + cap21,
                    "Capacitors,usuario=" + username + " cap22=" + cap22]
        return sequence

    def write_on_influx(self, sequence):
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        write_api.write(self.bucket, self.org, sequence)

    def save(self, user, val_sensores):
        flame = str(val_sensores[0])  # casteamos sensores a string
        touch = str(val_sensores[1])
        hum = str(val_sensores[2])
        temp = str(val_sensores[3])
        sequence = sequencify(user, hum, temp, flame, touch, touch, touch, touch)  # aquí habría que poner los capacitores
        print(sequence)
        write_on_influx(sequence)
