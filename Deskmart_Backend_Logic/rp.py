#!/usr/bin/python3

from grove_lib import grove_flame_sensor
from grove_lib import grove_infrarred_sensor #.Grove_Infrarred_Sensor
from grove_lib import grove_rgb_lcd #.Grove_Rgb_Lcd
from grove_lib import grove_temphum_sensor
from grove_lib import grove_touch_sensor

import config
import database_manager
import threading

import time

import datetime

class Runtime:
    def __init__(self):
        self.temp_hum = grove_temphum_sensor.Grove_TempHum_sensor(config.TEMP_HUM_SENSOR)

        self.flame = grove_flame_sensor.Grove_Flame_Sensor(config.FLAME_SENSOR)

        self.touch11 = grove_touch_sensor.GroveTouchSensor(config.TOUCH_SENSOR_1x1)
        self.touch12 = grove_touch_sensor.GroveTouchSensor(config.TOUCH_SENSOR_1x2)
        self.touch21 = grove_touch_sensor.GroveTouchSensor(config.TOUCH_SENSOR_2x1)
        self.touch22 = grove_touch_sensor.GroveTouchSensor(config.TOUCH_SENSOR_2x2)
        
        self.hum_value = 0
        self.temp_value = 0
        
        self.flame_value = 0
        
        self.touch11_value = 0
        self.touch12_value = 0
        self.touch21_value = 0
        self.touch22_value = 0
        
        self.lcd = grove_rgb_lcd.Grove_Rgb_Lcd()

        self.db = database_manager.InfluxController()

    def record(self):

        self.hum_value = self.temp_hum.read()[0]
        self.temp_value = self.temp_hum.read()[1]
        
        self.flame_value = self.flame.read()
        
        self.touch11_value = self.touch11.read()
        self.touch12_value = self.touch12.read()
        self.touch21_value = self.touch21.read()
        self.touch22_value = self.touch22.read()

        values = [self.hum_value, self.temp_value, self.flame_value, self.touch11_value, self.touch12_value, self.touch21_value, self.touch22_value]

        self.db.save(config.USERNAME, values)
        
    def work(self):
        while True:
            self.record()
            time.sleep(1)
        
    def terminal(self):
        
        while True:
            self.lcd.setRGB(125,0,0)
            self.lcd.setText("Username:\n{}".format(config.USERNAME))
            
            time.sleep(4)
            now = datetime.datetime.now()
            self.lcd.setRGB(0,0,125)
            self.lcd.setText("Date:\n{}/{}/{}".format(now.day, now.month, now.year))        
            time.sleep(4)
            
            self.lcd.setRGB(0,0,125)
            self.lcd.setText("Hour:\n{}:{}".format(now.hour+1, now.minute))
            time.sleep(4)
            
            self.lcd.setRGB(50,125,50)
            self.lcd.setText("Temp. inside:\n{}°C".format(self.temp_value))
            time.sleep(4)
            
            self.lcd.setRGB(50,125,50)
            self.lcd.setText("Humidity inside:\n{}%".format(self.hum_value))
            time.sleep(4)
            
            self.lcd.setRGB(75,50,50)
            text= "SAFE"
            if self.flame_value:
                text= "ALERT"
                
            self.lcd.setText("User temp.:\n{}".format(text))
            time.sleep(4)
            
            
        
        
if __name__ == '__main__':
    runtime = Runtime()
    hilo1 = threading.Thread(target=runtime.work)
    hilo2 = threading.Thread(target=runtime.terminal)
    hilo1.start()
    hilo2.start()