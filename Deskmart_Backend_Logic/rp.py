from grove_lib import grove_flame_sensor
from grove_lib import grove_infrarred_sensor #.Grove_Infrarred_Sensor
from grove_lib import grove_rgb_lcd #.Grove_Rgb_Lcd
from grove_lib import grove_temphum_sensor
from grove_lib import grove_touch_sensor

import config
import database_manager

def init():
    print("Initializing")
    temp_hum = grove_temphum_sensor.Grove_TempHum_sensor(config.TEMP_HUM_SENSOR)

    flame = grove_flame_sensor.Grove_Flame_Sensor(config.FLAME_SENSOR)

    touch11 = grove_touch_sensor.GroveTouchSensor(config.TOUCH_SENSOR_1x1)
    touch12 = grove_touch_sensor.GroveTouchSensor(config.TOUCH_SENSOR_1x2)
    touch21 = grove_touch_sensor.GroveTouchSensor(config.TOUCH_SENSOR_2x1)
    touch22 = grove_touch_sensor.GroveTouchSensor(config.TOUCH_SENSOR_2x2)
    print("Initializing finished")

    '''
    print("Going to read")
    
    print("Touch sensor {}".format(touch.read()))
    print("Temp_Hum sensor {}".format(temp_hum.read()))
    print("Flame sensor {}".format(flame.read()))
    '''

    return temp_hum, flame, touch11, touch12, touch21, touch22 

def record():
    temp_hum, flame, touch11, touch12, touch21, touch22 = init()

    hum_value = temp_hum.read()[0]
    temp_value = temp_hum.read()[1]
    
    flame_value = flame.read()
    
    touch11_value = touch11.read()
    touch12_value = touch12.read()
    touch21_value = touch21.read()
    touch22_value = touch22.read()

    values = [hum_value, temp_value, flame_value, touch11_value, touch12_value, touch21_value, touch22_value]

    db = database_manager.InfluxController()
    db.save("ibai", values)
    
if __name__ == '__main__':
    record()