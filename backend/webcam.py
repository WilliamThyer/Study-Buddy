import os
import pathlib
import time

import cv2


class Webcam():
    def __init__(self):
        self.capture = cv2.VideoCapture(0)

    def get_image(self):
        _, frame = self.capture.read()
        return frame

    def make_frame_folder(self, savedirbase='frames'):
        if not os.path.isdir(savedirbase):
            os.mkdir(savedirbase)

        counter = 1
        while True:
            folder_try = pathlib.Path(savedirbase)/str(counter)
            if os.path.isdir(folder_try):
                counter += 1
            else:
                os.mkdir(folder_try)
                break

        return folder_try

    def write_image_stream(self, length=5, wait=1):
        savedir = self.make_frame_folder()

        image_counter = 1
        start_time = time.time()

        while time.time() < start_time + length:
            frame = self.get_image()
            cv2.imwrite(str(savedir/f'{image_counter}.png'), frame)
            image_counter += 1
            time.sleep(wait)
