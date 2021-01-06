from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import config


class InfluxController:
    def __init__(self):
        self.org = "jorge.elbusto@opendeusto.es"
        self.bucket = "DeskMart"
        self.client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=config.INFLUXDB_TOKEN)
        
    
    def get_influx_data(self):
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

    def get_last_timestamp(self):
        results = self.get_influx_data()
        lastSensors = results[-7:]
        return lastSensors

    def get_last_flame(self):
        results = self.get_last_timestamp()
        for x in results:
            if "hayLlama" in x:
                return x

    def get_last_hum(self):
        results = self.get_last_timestamp()
        for x in results:
            if "hayLlama" in x:
                return x

    def get_last_temp(self):
        results = self.get_last_timestamp()
        for x in results:
            if "temperatura" in x:
                return x

    def get_capacitors_heatmap(self):
        results = self.get_influx_data()
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