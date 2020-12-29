import grovepi

import time
from grove.gpio import GPIO
 

class GroveTouchSensor(GPIO):
    def __init__(self, pin):
        super(GroveTouchSensor, self).__init__(pin, GPIO.IN)
        self._last_time = time.time()

        self._on_press = None
        self._on_release = None

    @property
    def on_press(self):
        return self._on_press

    @on_press.setter
    def on_press(self, callback):
        if not callable(callback):
            return

        if self.on_event is None:
            self.on_event = self._handle_event

        self._on_press = callback

    @property
    def on_release(self):
        return self._on_release

    @on_release.setter
    def on_release(self, callback):
        if not callable(callback):
            return

        if self.on_event is None:
            self.on_event = self._handle_event

        self._on_release = callback

    def _handle_event(self, pin, value):
        t = time.time()
        dt, self._last_time = t - self._last_time, t

        if value:
            if callable(self._on_press):
                self._on_press(dt)
        else:
            if callable(self._on_release):
                self._on_release(dt)

    def read(self):
        try:
            time.sleep(.5)
            touch = GroveTouchSensor("18", pin)

            def on_press(t):
                print('Pressed')
            def on_release(t):
               print("Released.")

            touch.on_press = on_press
            touch.on_release = on_release
            
            return touch

        except IOError:
            print ("Error")

# def main():
#     import sys
#
#     if len(sys.argv) < 2:
#         print('Usage: {} pin'.format(sys.argv[0]))
#         sys.exit(1)
#
#     touch = GroveTouchSensor(int(sys.argv[1]))
#
#     def on_press(t):
#         print('Pressed')
#     def on_release(t):
#         print("Released.")
#
#     touch.on_press = on_press
#     touch.on_release = on_release
#
#     while True:
#         time.sleep(1)
#
#
#
# class Grove_Touch_Sensor:
#     def __init__(self, pin):
#         # Connect the Grove Flame Sensor to digital port D2
#         # SIG,NC,VCC,GND
#         self.touch_sensor = pin
#         grovepi.pinMode(self.touch_sensor,"INPUT")
#
#     def read(self):
#         try:
#             time.sleep(.5)
#             return grovepi.digitalRead(self.touch_sensor)
#         except IOError:
#             print ("Error")