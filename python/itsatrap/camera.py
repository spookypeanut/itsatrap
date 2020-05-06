from time import sleep
from picamera import PiCamera


class Camera(object):
    def __init__(self):
        self.resolution = "1080p"

    def take_photo(self, filepath):
        with PiCamera() as camera:
            # Camera warm-up time
            camera.resolution = "1080p"
            sleep(.5)
            camera.capture(filepath)
