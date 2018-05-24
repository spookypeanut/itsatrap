from __future__ import division, absolute_import, print_function

import os
from datetime import datetime

from .pir import Pir
from .camera import Camera

DEFAULT_PHOTO_PATH = "/home/hbush/trapphotos"

class Trap(object):
    def __init__(self):
        self.pir = Pir()
        self.camera = Camera()

    def start_trap(self):
        def trap_function(pir_pin):
            base_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S.jpg")
            image_path = os.path.join(DEFAULT_PHOTO_PATH, base_name)
            self.camera.take_photo(image_path)

        self.pir.start_watching(trap_function)

    def stop_trap(self):
        self.pir.stop_watching()
