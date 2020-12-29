import grovepi

class Grove_Flame_Sensor:
    def __init__(self, pin):
        # Connect the Grove Flame Sensor to digital port D2
        # SIG,NC,VCC,GND
        self.flame_sensor = pin
        grovepi.pinMode(self.flame_sensor,"INPUT")
    
    def read(self):
        return self.grovepi.digitalRead(self.flame_sensor)