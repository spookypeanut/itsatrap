from __future__ import division, absolute_import, print_function

import os
from datetime import datetime

from .pir import Pir
from .camera import Camera

DEFAULT_PHOTO_PATH = "/home/hbush/trapphotos"


class Trap(object):
    def __init__(self, photos=True, verbose=False):
        self.pir = Pir()
        self.take_photos = photos
        self.verbose = verbose
        if self.take_photos is True:
            self.camera = Camera()
        else:
            self.camera = None

    def start_trap(self):
        def trap_function(pir_pin):
            base_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S.jpg")
            image_path = os.path.join(DEFAULT_PHOTO_PATH, base_name)
            if self.take_photos is True:
                self.camera.take_photo(image_path)
            if self.verbose is True:
                print("Triggered: %s" % image_path)

        self.pir.start_watching(trap_function)

    def stop_trap(self):
        self.pir.stop_watching()
