from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import config
import numpy as np



class InfluxController:
    def __init__(self):
        self.org = "jorge.elbusto@opendeusto.es"
        self.bucket = "DeskMart"
        self.client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=config.INFLUXDB_TOKEN)
        
    
    def get_influx_data(self, username):
        query = 'from(bucket: "DeskMart") |> range(start: -23h, stop: now()) |> filter(fn: (r) => r["_measurement"] == "Capacitors" or r["_measurement"] == "humTemp" or r["_measurement"] == "llama")'
        result = self.client.query_api().query(query, org=self.org)
        results = []
        for table in result:
            for record in table.records:
                results.append((record.get_time().strftime("%d/%m/%Y, %H:%M:%S"), record.get_field(), record.get_value()))

        results_ordenados = sorted(results, key=lambda tup: tup[0])

        for x in results_ordenados:
            print(x)

        return results_ordenados

    def get_last_timestamp(self, username):
        results = self.get_influx_data(username)
        lastSensors = results[-7:]
        return lastSensors

    def get_last_flame(self, username):
        results = self.get_last_timestamp(username)
        for x in results:
            if "hayLlama" in x:
                return x

    def get_last_hum(self, username):
        results = self.get_last_timestamp(username)
        for x in results:
            if "humedad" in x:
                return x

    def get_last_temp(self, username):
        results = self.get_last_timestamp(username)
        for x in results:
            if "temperatura" in x:
                return x

    def get_capacitors_heatmap(self, username):
        results = self.get_influx_data(username)
        puntCap11 = 0
        puntCap12 = 0
        puntCap21 = 0
        puntCap22 = 0
        for x in results:
            if "cap11" in x:
                if x[2] == 1.0:
                    puntCap11 += 1
            if "cap21" in x:
                if x[2] == 1.0:
                    puntCap21 += 1
            if "cap12" in x:
                if x[2] == 1.0:
                    puntCap12 += 1
            if "cap22" in x:
                if x[2] == 1.0:
                    puntCap22 += 1

        puntuaciones = {
          "cap11": puntCap11,
          "cap12": puntCap12,
          "cap21": puntCap21,
          "cap22": puntCap22
        }

        return puntuaciones

    def get_heatmap_colors(self, username):
        capacitorsScore = self.get_capacitors_heatmap(username)
        cap11 = capacitorsScore.get('cap11')
        cap12 = capacitorsScore.get('cap12')
        cap21 = capacitorsScore.get('cap21')
        cap22 = capacitorsScore.get('cap22')
        capacitors = [cap11, cap12, cap21, cap22]
        maxValue = int(np.max(capacitors))
        index = 0
        for x in capacitors:
            if maxValue != 0:
                if x / maxValue > 0.75:
                    capacitors[index] = "#FF0000"
                if x / maxValue > 0.5 and x / maxValue < 0.75:
                    capacitors[index] = "#FFA200"
                if x / maxValue > 0.25 and x / maxValue < 0.5:
                    capacitors[index] = "#FFDB00"
                if x / maxValue < 0.25:
                    capacitors[index] = "#2CAD00"
            else:
                capacitors = ["#2CAD00", "#2CAD00", "#2CAD00", "#2CAD00"]
            index += 1




        colors = {
            "cap11": capacitors[0],
            "cap12": capacitors[1],
            "cap21": capacitors[2],
            "cap22": capacitors[3],
        }
        return colors
