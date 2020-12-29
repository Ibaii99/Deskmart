from lib.grove_flame_sensor import Grove_Flame_Sensor
from lib.grove_infrarred_sensor import Grove_Infrarred_Sensor
from lib.grove_rgb_lcd import Grove_Rgb_Lcd
from lib.grove_temphum_sensor import Grove_TempHum_sensor
from lib.grove_touch_sensor import Grove_Touch_Sensor

import config


def init():
    print("Initializing")
    flame = Grove_Flame_Sensor(config.FLAME_SENSOR)
    touch = Grove_Touch_Sensor(config.TOUCH_SENSOR)
    temp_hum = Grove_TempHum_sensor(config.TEMP_HUM_SENSOR)
    print("Initializing finished")

    print("Going to read")
    print("Flame sensor {}".format(flame.read()))
    print("Touch sensor {}".format(touch.read()))
    print("Temp_Hum sensor {}".format(temp_hum.read()))
    

if __name__ == '__main__':
    init()
    