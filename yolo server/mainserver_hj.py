import cv2
import numpy as np
import threading
import time
import FrameProcess
import dataserver
import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'python/'))
sys.path.append(os.getcwd().replace('darknet', ''))
# sys.path.append(os.getcwd().replace('darknet', 'camData/'))
# sys.path.append(os.getcwd().replace('darknet', 'img1/'))


class MainThread:
    def __init__(self):
        self.ts = Telecommunication()
        self.ts.streaming()
        self.ts.streaming.after(1000, FrameProcess.frame2video())
        FrameProcess.frame2video.after(3000, self.runYolo())
        self.runYolo().after(3000, self.ts.sendcoordinates())

    def runYolo(self):
        # command: run yolo
        os.system(
            './darknet detector demo data/obj.data cfg/yolov3.cfg backup/yolov3_3300.weights '
            'data/media/video{},avi'.format(video_name_cnt))
        print("Now Detecting Black Ice...")


MainThread()