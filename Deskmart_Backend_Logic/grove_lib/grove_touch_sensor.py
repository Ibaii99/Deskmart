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

class Grove_Touch_Sensor():
    def __init__ (self, pin):
        self.touch = GroveTouchSensor(int(pin))
 
    def on_press(self, t):
        print('Pressed')

    def on_release(self, t):
        print("Released.")
 
    def read(self):
        self.touch.on_press = on_press
        self.touch.on_release = on_release
        if self.touch.on_press:
            return 1
        elif self.touch.on_release:
            return 0