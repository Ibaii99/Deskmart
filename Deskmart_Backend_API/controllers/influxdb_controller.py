from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import config, logging
import numpy as np



class InfluxController:
    def __init__(self):
        self.org = "jorge.elbusto@opendeusto.es"
        self.bucket = "DeskMart"
        self.client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=config.INFLUXDB_TOKEN)
        
    
    def get_influx_data(self, username):
        query = 'from(bucket: "DeskMart") |> range(start: -3h, stop: now()) |> filter(fn: (r) => r["_measurement"] == "Capacitors" or r["_measurement"] == "humTemp" or r["_measurement"] == "llama") |> filter(fn: (r) => r["usuario"] == "' + username + '")'
        result = self.client.query_api().query(query, org=self.org)
        results = []
        for table in result:
            for record in table.records:
                results.append((record.get_time().strftime("%d/%m/%Y, %H:%M:%S"), record.get_field(), record.get_value()))

        results_ordenados = sorted(results, key=lambda tup: tup[0])

        return results_ordenados

    def get_user_history(self, username):
        query = 'from(bucket: "DeskMart") |> range(start: -30d, stop: now()) |> filter(fn: (r) => r["_measurement"] == "Capacitors" or r["_measurement"] == "humTemp" or r["_measurement"] == "llama") |> filter(fn: (r) => r["usuario"] == "' + username + '")'
        result = self.client.query_api().query(query, org=self.org)
        results = []
        for table in result:
            for record in table.records:
                results.append((record.get_time().strftime("%d/%m/%Y, %H:%M:%S"), record.get_field(), record.get_value()))

        results_ordenados = sorted(results, key=lambda tup: tup[0])

        return results_ordenados

    def get_by_day(self, username, day, month, year):
        query = 'from(bucket: "DeskMart") |> range(start: ' + year + '-' + month + '-' + day + 'T00:00:00Z, stop: ' + year + '-' + month + '-' + day + 'T23:59:59Z) |> filter(fn: (r) => r["_measurement"] == "Capacitors" or r["_measurement"] == "humTemp" or r["_measurement"] == "llama") |> filter(fn: (r) => r["usuario"] == "' + username + '")'
        result = self.client.query_api().query(query, org=self.org)
        results = []
        for table in result:
            for record in table.records:
                results.append(
                    (record.get_time().strftime("%d/%m/%Y, %H:%M:%S"), record.get_field(), record.get_value()))
        
        results_ordenados = sorted(results, key=lambda tup: tup[0])
        return results_ordenados

    def get_by_range(self, username, dayFrom, monthFrom, yearFrom, dayTo, monthTo, yearTo):
        query = 'from(bucket: "DeskMart") |> range(start: ' + yearFrom + '-' + monthFrom + '-' + dayFrom + 'T00:00:00Z, stop: ' + yearTo + '-' + monthTo + '-' + dayTo + 'T23:59:59Z) |> filter(fn: (r) => r["_measurement"] == "Capacitors" or r["_measurement"] == "humTemp" or r["_measurement"] == "llama") |> filter(fn: (r) => r["usuario"] == "' + username + '")'
        result = self.client.query_api().query(query, org=self.org)
        results = []
        for table in result:
            for record in table.records:
                results.append((record.get_time().strftime("%d/%m/%Y, %H:%M:%S"), record.get_field(), record.get_value()))

        results_ordenados = sorted(results, key=lambda tup: tup[0])

        return results_ordenados

    def get_last_timestamp_by_day(self, username, day, month, year):
        results = self.get_by_day(username, day, month, year)
        lastSensors = results[-7:]
        return lastSensors

    def get_last_timestamp(self, username):
        results = self.get_user_history(username)
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

    def get_capacitors_heatmap(self, username, day, month, year):
        results = self.get_by_day(username, day, month, year)
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
    
    def get_capacitors_touch_time(self, username, day, month, year):
        results = self.get_by_day(username, day, month, year)
        times = 0
        previusTimestamp = None
        to_add = True
        for x in results:
            if previusTimestamp is None or previusTimestamp!= x[0]:
                previusTimestamp= x[0]
                to_add = True
                
            if "cap11" in x and to_add:
                if x[2] == 1.0:
                    times += 1
                    to_add = False
            
            if "cap12" in x and to_add:
                if x[2] == 1.0:
                    times += 1
                    to_add = False
            
            if "cap21" in x and to_add:
                if x[2] == 1.0:
                    times += 1
                    to_add = False
            
            if "cap22" in x and to_add:
                if x[2] == 1.0:
                    times += 1
                    to_add = False

        return times
    
    def get_heatmap_colors(self, username, day, month, year):
        capacitorsScore = self.get_capacitors_heatmap(username, day, month, year)
        cap11 = capacitorsScore.get('cap11')
        cap12 = capacitorsScore.get('cap12')
        cap21 = capacitorsScore.get('cap21')
        cap22 = capacitorsScore.get('cap22')
        capacitors = [cap11, cap12, cap21, cap22]
        maxValue = int(np.max(capacitors))
        index = 0
        for x in capacitors:
            if maxValue != 0:
                if x / maxValue > 0.75 and x / maxValue <= 1:
                    capacitors[index] = "#FF0000"
                if x / maxValue > 0.5 and x / maxValue <= 0.75:
                    capacitors[index] = "#FFA200"
                if x / maxValue > 0.25 and x / maxValue <= 0.5:
                    capacitors[index] = "#FFDB00"
                if x / maxValue < 0.25 and x != 0:
                    capacitors[index] = "#a5cf00"
                if x == 0:
                    capacitors[index] = "#2CAD00"
            else:
                capacitors = ["#2CAD00", "#2CAD00", "#2CAD00", "#2CAD00"]
            index += 1
        colors = {
            "cap11": capacitors[0],
            "cap12": capacitors[1],
            "cap21": capacitors[2],
            "cap22": capacitors[3],
            "maxValue": maxValue
        }
        return colors

    def get_distinct_days(self, username):
        results = self.get_user_history(username)
        distinct_dates = []
        for x in results:
            arrFecha = x[0].split(",")
            fecha = arrFecha[0]
            if fecha not in distinct_dates:
                distinct_dates.append(fecha)
        logging.warning(distinct_dates)
        return distinct_dates
