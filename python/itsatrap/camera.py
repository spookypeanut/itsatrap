from time import sleep
from picamera import PiCamera


class Camera(object):
    def __init__(self):
        self._picamera = PiCamera()
        self._picamera.resolution = "1080p"

    def take_photo(self, filepath):
        self._picamera.start_preview()
        # Camera warm-up time
        sleep(.5)
        self._picamera.capture(filepath)

