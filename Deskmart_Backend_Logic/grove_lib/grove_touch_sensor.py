import grovepi

class Grove_Touch_Sensor:
    def __init__(self, pin):
        # Connect the Grove Flame Sensor to digital port D2
        # SIG,NC,VCC,GND
        self.touch_sensor = pin
        grovepi.pinMode(self.touch_sensor,"INPUT")
    
    def read(self):
        return grovepi.digitalRead(self.touch_sensor)