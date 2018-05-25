import RPi.GPIO as GPIO

PIR_PIN = 7

class Pir(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIR_PIN, GPIO.IN)

    def __del__(self):
        GPIO.cleanup()

    def start_watching(self, on_trap_call):
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=on_trap_call)

    def stop_watching(self):
        GPIO.remove_event_detect(PIR_PIN)

