from socket import *
import socket
import cv2
import numpy as np
import threading
import time
import FrameProcess as fp
import sys
import os
# sys.path.append(os.path.join(os.getcwd(), 'python/'))
# sys.path.append(os.getcwd().replace('darknet', ''))
# sys.path.append(os.getcwd().replace('darknet', 'camData/'))
# sys.path.append(os.getcwd().replace('darknet', 'img1/'))


# image file path
src = "./camData"


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


def streaming():
    # server socket
    host = "192.168.255.21"
    port = 5003
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    # waiting client
    server_socket.listen(5)
    print('Server Socket is listening')

    # IMG & VIDEO FILE NAME COUNT
    frame_cnt = 0
    img_filename_cnt = 1

    for _ in range(2):
        # establish connection with client (conn: client socket, addr: binded address)
        conn, addr = server_socket.accept()
        print('Connected to :', addr[0], ':', addr[1])

        while True:
            print("############## run ###############")

            # GET CAM IMG
            # receive cam data
            length = recvall(conn, 16)
            stringData = recvall(conn, int(length))
            print('# get string_data')
            data = np.fromstring(stringData, dtype='uint8')
            print('### get self.data')
            frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
            print('##### decode self.data')
            # print(np.shape(frame))
            # print("frame : ", frame)
            # print("shape :", frame.shape)
            '''
            # count the number of frames
            frame_cnt += 1
            if (frame_cnt > 600):
                img_filename_cnt += 1
            '''
            # streaming
            # print("frame: ",frame)
            cv2.imshow("Streaming", frame)
            cv2.waitKey(5)

        # store cam frames
        cv2.imwrite('/img{}/cam{}.jpg'.format(img_filename_cnt, frame_cnt), frame)
        print('Store frames at FILE: img' + img_filename_cnt + ' Successfully')

        '''
        # FRAME TO VIDEO
        # get img file
        img_path = src + '/img' + img_filename_cnt
        '''


# Send_open/read file
class SendCoordinates(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.data = np.zeros(0)

    def run(self):
        global conn
        global video_name_cnt
        while True:
            # read yolo_mark bounding box
            f = open("/home/heejunghong/BlackfencerWeb/index.html", 'r')
            self.data = f.read()
            conn.send(str(self.data))
            f.close()

    def shutdown(self):
        pass


if __name__ == '__main__':
    main()
