import RPi.GPIO as GPIO
from datetime import datetime, timedelta

PIR_PIN = 7
NUM_TIMES = 3
NUM_SECONDS = 1

class Pir(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIR_PIN, GPIO.IN)
        self.previous = []
        self.on_trap_call = None

    def __del__(self):
        GPIO.cleanup()

    def _clear_old(self):
        oldest = datetime.now() - timedelta(seconds=NUM_SECONDS)
        for d in self.previous:
            if d < oldest:
                self.previous.remove(d)

    def buffered_call(self, on_trap_call):
        self.previous.append(datetime.now())
        self._clear_old()
        print(self.previous)
        if len(self.previous) >= NUM_TIMES:
            on_trap_call()

    def start_watching(self, on_trap_call):
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=on_trap_call)

    def start_buffered_watching(self, on_trap_call):
        self.on_trap_call = on_trap_call
        callback = self.buffered_call
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=callback)

    def stop_watching(self):
        GPIO.remove_event_detect(PIR_PIN)
