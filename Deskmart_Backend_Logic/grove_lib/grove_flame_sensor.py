import RPi.GPIO as GPIO

class Grove_Flame_Sensor:

    def __init__(self, pin):
        # SIG,NC,VCC,GND
        # self.flame_sensor = pin
        # grovepi.pinMode(self.flame_sensor,"INPUT")
        GPIO.setmode(GPIO.BCM)
        self.INPUT_PIN = pin
        GPIO.setup(self.INPUT_PIN, GPIO.IN)
        input = GPIO.input(self.INPUT_PIN)
    
    def read(self):
        if (GPIO.input(self.INPUT_PIN) == True): # Physically read the pin now
            return 0
        else:
            return 1