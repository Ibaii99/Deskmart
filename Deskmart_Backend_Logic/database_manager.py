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
        print("Write finished")

    def save(self, user, val_sensores):
        hum = str(val_sensores[0])
        temp = str(val_sensores[1])
        
        flame = str(val_sensores[2])  # casteamos sensores a string
        
        touch11 = str(val_sensores[1])
        touch12 = str(val_sensores[1])
        touch21 = str(val_sensores[1])
        touch22 = str(val_sensores[1])

        
        sequence = self.sequencify(user, hum, temp, flame, touch11, touch12, touch21, touch22)  # aquí habría que poner los capacitores
        
        print("Sequence: {}".format(sequence))
        
        self.write_on_influx(sequence)
