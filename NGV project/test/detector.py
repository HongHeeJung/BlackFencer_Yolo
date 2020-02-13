import cv2
import numpy as np
import threading
import socket
import os, sys, time
import shutil


class RunYolo(threading.Thread):
    # printLog = pyqtSignal(str)
    workingFlag = 0

    def run(self):
        try:
            self.workingFlag = 1
            self.printLog.emit("Analysis Initializing...")
            sys.path.append(os.path.join(os.getcwd(), 'darknet/python/'))
            sys.path.append(os.path.join(os.getcwd()))
            import darknet as dn
            import pdb

            dn.set_gpu(0)
            net = dn.load_net("darknet/cfg/yolov3.cfg".encode('utf-8'),
                              "darknet/backup/yolov3_3300.weights".encode('utf-8'), 0)
            meta = dn.load_meta("darknet/cfg/coco.data".encode('utf-8'))

            path = 'camData/'
            file_list = os.listdir(path)
            if ".USED" in file_list:
                file_list.remove(".USED")

            total_file_num = len(file_list)
            current_file_num = int()

            if os.path.isfile('detection_result.txt'):
                os.remove('detection_result.txt')
            f = open('detection_result.txt', 'a')

            self.printLog.emit("Start Analysis...")
            for file_name in file_list:
                self.printLog.emit("Analysing... " + str(current_file_num) + '/' + str(total_file_num))
                filepath = path + file_name
                r = dn.detect(net, meta, filepath.encode('utf-8'))

                current_file_num = current_file_num + 1
                print(str(current_file_num) + '///' + str(total_file_num))

                if r:
                    print(r)
                    print(file_name)

                    f.write(file_name)
                    f.write('\n')

            f.close()
            self.printLog.emit("Analysing... " + str(current_file_num) + '/' + str(total_file_num))
            self.printLog.emit("Analysing Finished!")
            self.workingFlag = 0
            print("DARKNET END")

        except OSError:
            self.printLog.emit("Darknet Faild to start!")
            self.printLog.emit("Darknet Reinitializing...")

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

            self.printLog.emit("Darknet Reinitializing Finished")
            self.printLog.emit("Please try again Analysis")
            self.workingFlag = 0

