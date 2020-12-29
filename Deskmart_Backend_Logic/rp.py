from Deskmart_Backend_Logic.grove_lib import grove_flame_sensor
from Deskmart_Backend_Logic.grove_lib import grove_infrarred_sensor #.Grove_Infrarred_Sensor
from Deskmart_Backend_Logic.grove_lib import grove_rgb_lcd #.Grove_Rgb_Lcd
from Deskmart_Backend_Logic.grove_lib import grove_temphum_sensor
from Deskmart_Backend_Logic.grove_lib import grove_touch_sensor

import config


def init():
    print("Initializing")
    flame = grove_flame_sensor.Grove_Flame_Sensor(config.FLAME_SENSOR)
    touch = grove_touch_sensor.Grove_Touch_Sensor(config.TOUCH_SENSOR)
    temp_hum = grove_temphum_sensor.Grove_TempHum_sensor(config.TEMP_HUM_SENSOR)
    print("Initializing finished")

    print("Going to read")
    print("Touch sensor {}".format(touch.read()))
    print("Temp_Hum sensor {}".format(temp_hum.read()))
    
    print("Flame sensor {}".format(flame.read()))

if __name__ == '__main__':
    init()
    