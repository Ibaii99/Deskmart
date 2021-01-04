import grovepi



import RPi.GPIO as GPIO


class Grove_Flame_Sensor:

    def __init__(self, pin):
        # SIG,NC,VCC,GND
        # self.flame_sensor = pin
        # grovepi.pinMode(self.flame_sensor,"INPUT")
        GPIO.setmode(GPIO.BCM)
        self.INPUT_PIN = 22
        GPIO.setup(self.INPUT_PIN, GPIO.IN)
        input = GPIO.input(self.INPUT_PIN)
    
    def read(self):
        if (GPIO.input(self.INPUT_PIN) == True): # Physically read the pin now
            return 1
        else:
            return 0
        #return grovepi.digitalRead(self.flame_sensor)