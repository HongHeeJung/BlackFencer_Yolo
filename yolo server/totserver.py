from socket import *
import socket
import cv2
import numpy as np
import threading
import time
# import random
# import re # extract number
import sys, os
# sys.path.append(os.path.join(os.getcwd(), 'python/'))
# sys.path.append(os.getcwd().replace('darknet', ''))
# sys.path.append(os.getcwd().replace('darknet', 'camData/'))
# sys.path.append(os.getcwd().replace('darknet', 'img1/'))
import FrameProcess as fp

# image file path
src = "./camData"

# server socket
host = "192.168.255.21"
port = 5003
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
# waiting client
sock.listen(5)
print('Server Socket is listening')
# establish connection with client (conn: client socket, addr: binded address) 
conn, addr = sock.accept()
print('Connected to :', addr[0], ':', addr[1])


def main():
    mystreaming = Streaming()
    mystreaming.start()
    time.sleep(5)
    mysendcoords = SendCoordinates()
    mysendcoords.start()
    myyolovideo = YoloVideo()
    myyolovideo.start()
    time.sleep(5)

'''
# Handler
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self)
        print(self.
'''


# Streaming_return buffer
def recvall(sock, count):    
    print("ok")
    buf = b''
    while count:
        newbuf = sock.recv(count)
        print("newbuf: ", newbuf)
        print("count: ", count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


# IMG & VIDEO FILE NAME COUNT
img_filename_cnt = 1
video_name_cnt = 1

length = recvall(conn, 16)
stringData = "1"
data = "1"


# _lock = threading.Lock()
class Streaming:
    def __init__(self):
        threading.Thread.__init__(self)

        # stringData size (==(str(len(stringData))).encode().ljust(16))
        # length = recvall(conn, 16)
        # self.stringData = 1
        # self.data = 1
        print("Streaming mainThread Start")
        
    def run(self):
        global conn
        global length
        global stringData
        global data
        global img_filename_cnt
        global video_name_cnt
        while True:
            print("############## run ###############")
            # lock aquired by client
            # _lock.acquire()

            # GET CAM IMG
            # receive cam data
            stringData = recvall(conn, int(length))
            print('# get string_data    ', stringData)
            data = np.fromstring(stringData, dtype=np.uint8)
            print('### get self.data')
            frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
            print('##### decode self.data')
            # print(np.shape(frame))
            # print("frame : ", frame)
            # print("shape :", frame.shape)
            '''
            # count the number of frames
            frame_cnt = 0
            frame_cnt += 1
            if(frame_cnt > 600):
                img_filename_cnt += 1

            # store am frames
            # cv2.imwrite('/img'+img_filename_cnt+'/cam'+frame_cnt+'.jpg', frame)
            cv2.imwrite('/img{}/cam{}.jpg'.format(img_filename_cnt, frame_cnt), frame)
            print('Store frames at FILE: img' + img_filename_cnt + ' Successfully')
            '''
            # streaming
            # print("frame: ",frame)
            cv2.imshow("Streaming", frame)
            cv2.waitKey(5)
            # _lock.release()
            '''
            # FRAME TO VIDEO
            # get img file
            img_path = src + '/img' + img_filename_cnt
            # command: make mp4 file
            os.system("ffmpeg -f image2 -i " + img_path + "/cam%4d.jpg camData/media/video" + video_name_cnt + ".mp4")
            video_name_cnt += 1
            print('Make video' + video_name_cnt + ' Successfully')
            '''


class YoloVideo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global video_name_cnt
        while True:
            # command: run yolo
            os.system("./darknet detector demo data/obj.data cfg/yolov3.cfg backup/yolov3_3300.weights camData/media/video" + video_name_cnt + ".mp4")
            print("Now Detecting Black Ice...")


# Send_open/read file
class SendCoordinates(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.data = np.zeros(0)

    def run(self):
        global conn
        while True:
            time.sleep(0.1)
            # read yolo_mark bounding box
            f = open("/home/heejunghong/BlackfencerWeb/index.html", 'r')
            self.data = f.read()
            conn.send(str(self.data))
            f.close()


if __name__ == '__main__':
    main()
