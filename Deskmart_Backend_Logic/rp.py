from grove_lib import grove_flame_sensor
from grove_lib import grove_infrarred_sensor #.Grove_Infrarred_Sensor
from grove_lib import grove_rgb_lcd #.Grove_Rgb_Lcd
from grove_lib import grove_temphum_sensor
from grove_lib import grove_touch_sensor

from Deskmart_Backend_Logic import config
from Deskmart_Backend_Logic import database_manager

def init():
    print("Initializing")
    flame = grove_flame_sensor.Grove_Flame_Sensor(config.FLAME_SENSOR)
    touch = grove_touch_sensor.GroveTouchSensor(config.TOUCH_SENSOR)
    temp_hum = grove_temphum_sensor.Grove_TempHum_sensor(config.TEMP_HUM_SENSOR)
    print("Initializing finished")

    print("Going to read")
    '''
    print("Touch sensor {}".format(touch.read()))
    print("Temp_Hum sensor {}".format(temp_hum.read()))
    print("Flame sensor {}".format(flame.read()))
    '''

    return flame, touch, temp_hum

def record():
    flame, touch, temp_hum = init()

    flameValue = flame.read()
    touchValue = touch.read()
    humValue = temp_hum.read()[0]
    tempValue = temp_hum.read()[1]

    values = [flameValue, touchValue, humValue, tempValue]

    db = database_manager.InfluxController()
    db.save("ibai", values)
    
if __name__ == '__main__':
    record()