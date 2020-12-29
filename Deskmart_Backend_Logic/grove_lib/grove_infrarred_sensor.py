import grovepi

class Grove_Infrarred_Sensor:
    def __init__(self, emitter_pin, receiver_pin):
        # Connect the Grove Flame Sensor to digital port D2
        # SIG,NC,VCC,GND
        self.infrarred_receiver = receiver_pin
        self.infrarred_emitter = emitter_pin
        grovepi.pinMode(self.infrarred_receiver,"INPUT")
        grovepi.pinMode(self.infrarred_emitter,"OUTPUT")
    
    def read(self):
        return grovepi.digitalRead(self.infrarred_receiver)

    def emit(self):
        return grovepi.digitalWrite(self.infrarred_emitter, 1)
    
    def stop(self):
        return grovepi.digitalWrite(self.infrarred_emitter, 0)