import grovepi



import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
INPUT_PIN = 22
GPIO.setup(INPUT_PIN, GPIO.IN)
input = GPIO.input(0)

class Grove_Flame_Sensor:

    def __init__(self, pin):
        # SIG,NC,VCC,GND
        self.flame_sensor = pin
        grovepi.pinMode(self.flame_sensor,"INPUT")
    
    def read(self):
        if (GPIO.input(INPUT_PIN) == True): # Physically read the pin now
            print('3.3')
        else:
            print('0')
        #return grovepi.digitalRead(self.flame_sensor)