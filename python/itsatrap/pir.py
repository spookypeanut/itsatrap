import RPi.GPIO as GPIO
from datetime import datetime, timedelta


""" A class for the PIR sensor. I use the HC-SR501:
https://thepihut.com/products/pir-infrared-motion-sensor-hc-sr501
https://www.mpja.com/download/31227sc.pdf
http://henrysbench.capnfatz.com/henrys-bench/arduino-sensors-and-input/arduino-hc-sr501-motion-sensor-tutorial/
"""

PIR_PIN = 7
NUM_TIMES = 3
NUM_SECONDS = 1


class Pir(object):
    def __init__(self):
        # The pin numbering system to use
        GPIO.setmode(GPIO.BCM)
        # Tell it which input pin to use
        GPIO.setup(PIR_PIN, GPIO.IN)
        # previous contains a list of the datetimes of all the triggers
        # in the last NUM_SECONDS (when using buffered_call)
        self.previous = []
        # The function to call when the IR detector is triggered
        self.on_trap_call = None

    def __del__(self):
        GPIO.cleanup()

    def _clear_old(self):
        """ Delete any trigger events from self.previous that are too old """
        # The oldest that events in the previous list can be
        oldest = datetime.now() - timedelta(seconds=NUM_SECONDS)
        for d in self.previous:
            if d < oldest:
                self.previous.remove(d)

    def buffered_call(self, on_trap_call):
        """ Only call the triggered function if the detector is triggered
        NUM_TIMES times within NUM_SECONDS seconds.
        """
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
