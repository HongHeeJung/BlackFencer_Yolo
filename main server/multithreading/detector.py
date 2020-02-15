#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import threading
from multiprocessing import Process
import socket
import os, sys, time
import shutil
'''
hj
'''

class RunYolo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print("[Threade] DARKNET")                       
        sys.path.append(os.path.join(os.getcwd(), 'python/'))
        import darknet as dn
        import pdb           
        print("Import successfully...")
                
        dn.set_gpu(0)
        self.net = dn.load_net("cfg/yolov3.cfg".encode('utf-8'),
                                  "backup/yolov3_3300.weights".encode('utf-8'), 0)
        self.meta = dn.load_meta("cfg/coco.data".encode('utf-8'))
        print("========================== WAITING... ============================")
        
    def run(self):
        sys.path.append(os.path.join(os.getcwd(), 'python/'))
        import darknet as dn
        import pdb
        while True:
            try:
                print("========================= DARKNET START ===========================")                
                print("Analysis Initializing...")
                '''
                self.workingFlag = 1
                print("Analysis Initializing...")
                sys.path.append(os.path.join(os.getcwd(), 'python/'))
                print("PATH 1")

                import darknet as dn
                import pdb           
                print("Import successfully...")
                
                dn.set_gpu(0)
                net = dn.load_net("cfg/yolov3.cfg".encode('utf-8'),
                                  "backup/yolov3_3300.weights".encode('utf-8'), 0)
                meta = dn.load_meta("cfg/coco.data".encode('utf-8'))
                '''
                '''                
                path = 'camData/'
                file_list = os.listdir(path)
                
                if ".USED" in file_list:
                    file_list.remove(".USED")

                total_file_num = len(file_list)
                current_file_num = int()
                '''
                if os.path.isfile('detection_result.txt'):
                    os.remove('detection_result.txt')
                f = open('detection_result.txt', 'a')

                print("Start Analysis...")
                frame_path = 'camData/image.jpg'
                r = dn.detect(self.net, self.meta, frame_path.encode('utf-8'))
                print("RESULT!!!!!!!!!!!!!!!!!!!!!!!!!!!!", r)
                '''
                for file_name in file_list:
                    print("Analysing... " + str(current_file_num) + '/' + str(total_file_num))
                    filepath = path + file_name
                    r = dn.detect(net, meta, filepath.encode('utf-8'))

                    current_file_num = current_file_num + 1
                    print(str(current_file_num) + '///' + str(total_file_num))

                    if r:
                        print(r)
                        print(file_name)

                        f.write(file_name)
                        f.write('\n')
                '''
                f.close()
                
                # self.printLog.emit("Analysing... " + str(current_file_num) + '/' + str(total_file_num))
                print("Analysing Finished!")               
                time.sleep(3)
                
                break
                
            # except OSError:
            except Exception as ex:
                print('detector.py ERROR', ex)
                break
            
            
            print("Darknet Faild to start!")
            print("Darknet Reinitializing...")

            if os.path.isfile("darknet/libdarknet.so"):
                os.remove("darknet/libdarknet.so")
            if os.path.isfile("darknet/libdarknet.a"):
                os.remove("darknet/libdarknet.a")
            if os.path.isfile("darknet/darknet"):
                os.remove("darknet/darknet")
            if os.path.isdir("darknet/obj/"):
                shutil.rmtree("darknet/obj/")

            makepath = os.getcwd() + "/darknet"
            os.system("make -C " + makepath)

            print("Darknet Reinitializing Finished")
            print("Please try again Analysis")
            self.workingFlag = 0
            
    def __del__(self):
        self.myRunYolo.close()
        print("========================= DARKNET END =============================")
            
            
            
            



'''
# DEFAULT DETECTOR.py 
# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

import sys, os
sys.path.append(os.path.join(os.getcwd(),'python/'))

import darknet as dn
import pdb

dn.set_gpu(0)
net = dn.load_net("cfg/yolo-thor.cfg", "/home/pjreddie/backup/yolo-thor_final.weights", 0)
meta = dn.load_meta("cfg/thor.data")
r = dn.detect(net, meta, "data/bedroom.jpg")
print r

# And then down here you could detect a lot more images like:
r = dn.detect(net, meta, "data/eagle.jpg")
print r
r = dn.detect(net, meta, "data/giraffe.jpg")
print r
r = dn.detect(net, meta, "data/horses.jpg")
print r
r = dn.detect(net, meta, "data/person.jpg")
print r
'''
