import time
import numpy as np
import cv2
import random
from fastai.vision import *

from gooey import Gooey, GooeyParser

import webcam
from punish import *

class Study_Buddy:
    def __init__(self):
        self.distracted_tracker = np.zeros(8)
        self.inattn_counter = 0
        self.wb = webcam.Webcam()
        self.punish_mode = 'Off'

    def load_model(self):
        self.learn = load_learner('.', 'model.pkl')

    @Gooey(program_name='Study Buddy', image_dir='./icons')
    def get_minutes(self):
        
        min_list = ['1','2','5','10','15','30','45','60']
        parser = GooeyParser(description="The study buddy you love to hate")
        parser.add_argument(
            "Timer",
            help="How many minutes do you want to stay focused for?",
            choices=min_list,
            nargs="*",
            widget="Dropdown"
        )

        args = parser.parse_args()
        self.minutes = int(args.Timer[0])*60
    
    def study_timer(self):

        start_time = time.time()
        while time.time() < start_time + self.minutes:
                frame = self.wb.convert_to_fastai(self.wb.get_image())
                result = self.attention_classifier(frame)
                result = str(result[0])
                self.handle_classification(result)
                time.sleep(1)

    def handle_classification(self,result):

        self.distracted_tracker = np.roll(self.distracted_tracker,1)
        print(result)
        if result == 'attend':
            self.distracted_tracker[0] = 0
        if result == 'nonattend':
            self.distracted_tracker[0] = 1

        if sum(self.distracted_tracker) >= 5:
            self.punish_mode = 'On'
            self.inattn_counter += 1
            punish(self.inattn_counter)
        elif self.punish_mode == 'On':
            self.punish_mode = 'Off'
            self.inattn_counter = 0
    
    def attention_classifier(self,frame):
        return self.learn.predict(frame)
        
sb = Study_Buddy()
sb.load_model()
sb.get_minutes()
sb.study_timer()