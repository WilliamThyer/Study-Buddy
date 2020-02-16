import time
import numpy as np
import cv2
import random
from fastai.vision import *
import matplotlib.pyplot as plt

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
        self.length = int(args.Timer[0])*60
    
    def study_timer(self):

        start_time = time.time()
        self.output = []
        while time.time() < start_time + self.length:
                frame = self.wb.convert_to_fastai(self.wb.get_image())
                result = self.attention_classifier(frame)
                result = str(result[0])
                self.handle_classification(result)
                if result == 'nonattend' and self.punish_mode == 'On':
                    pass
                else:
                    time.sleep(.75)

    def handle_classification(self,result):

        self.distracted_tracker = np.roll(self.distracted_tracker,1)
        print(result)
        if result == 'attend':
            self.distracted_tracker[0] = 0
            self.output.append(0)
        if result == 'nonattend':
            self.distracted_tracker[0] = 1
            self.output.append(1)

        if sum(self.distracted_tracker) >= 6:
            self.punish_mode = 'On'
            self.inattn_counter += 1
            punish(self.inattn_counter)
        elif self.punish_mode == 'On':
            self.punish_mode = 'Off'
            self.inattn_counter = 0
    
    def attention_classifier(self,frame):
        return self.learn.predict(frame)
    
    def plot_attention(self):
        data = self.running_mean(np.invert(np.array(self.output)))
        plt.plot(np.arange(0,len(data)),data)
        plt.xlabel('Study Time')
        plt.ylabel('Concentration Score')
        plt.title('Study Buddy Report')
        plt.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            labelbottom=False) # labels along the bottom edge are off
        plt.tick_params(
            axis='y',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            left=False,      # ticks along the bottom edge are off
            labelleft=False) # labels along the bottom edge are off
        
        plt.show()
        plt.savefig('test.png')

    def running_mean(self,data):
        cumsum = np.cumsum(np.insert(data, 0, 0)) 
        return (cumsum[10:] - cumsum[:-10]) / float(10)
        
sb = Study_Buddy()
sb.load_model()
sb.get_minutes()
sb.wb.show_align_face_window(delay=5)
sb.study_timer()
sb.plot_attention()
