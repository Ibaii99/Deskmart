from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import config


class InfluxController:
    def __init__(self):
        self.org = "jorge.elbusto@opendeusto.es"
        self.bucket = "DeskMart"
        self.client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=config.INFLUXDB_TOKEN)
        
    
    def get_influx_data(self):
        query = 'from(bucket: "DeskMart") |> range(start: -12h, stop: now()) |> filter(fn: (r) => r["_measurement"] == "Capacitors" or r["_measurement"] == "humTemp" or r["_measurement"] == "llama")' #FALLA LA QUERY
        result = self.client.query_api().query(query, org=self.org)
        results = []
        for table in result:
            for record in table.records:
                results.append((record.get_time().strftime("%m/%d/%Y, %H:%M:%S"), record.get_field(), record.get_value()))

        results_ordenados = sorted(results, key=lambda tup: tup[0])

        for x in results_ordenados:
            print(x)

        return results_ordenados


    def get_last_timestamp(self):
        results = getInfluxData()
        lastSensors = results.slice(Math.max(arr.length - 7, 1))
        return lastSensors
