import os
import pathlib
import time
#from fastai.vision import *
import cv2


class Webcam():
    def __init__(self):
        self.capture = cv2.VideoCapture(0)

    def get_image(self):
        _, frame = self.capture.read()
        return frame

    def show_align_face_window(self, delay=5):
        cv2.namedWindow('Align face...', cv2.WINDOW_NORMAL)

        start_time = time.time()
        while time.time() < start_time + delay:
            frame = self.get_image()
            cv2.resizeWindow('Align face...', 480, 270)
            cv2.imshow('Align face...', frame)
            cv2.waitKey(delay)
        cv2.destroyAllWindows()

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

    def convert_to_fastai(self, frame):
        img_fastai = Image(pil2tensor(frame, dtype=np.float32).div_(255))
        return img_fastai


wb = Webcam()
wb.show_align_face_window()
