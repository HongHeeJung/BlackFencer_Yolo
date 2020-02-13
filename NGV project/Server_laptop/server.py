'''
2020.02.13.
raspberry pi to Yolo server: RECEIVE JUST ONE FRAME
'''

from socket import *
import socket, select
import cv2
import numpy as np
import time
import sys
import os

# sys.path.append(os.path.join(os.getcwd(), 'python/'))
# sys.path.append(os.getcwd().replace('darknet', ''))
# sys.path.append(os.getcwd().replace('darknet', 'camData/'))
# sys.path.append(os.getcwd().replace('darknet', 'img1/'))


class Telecommunication:
    def __init__(self):
        # server socket
        self.host = "192.168.255.21"
        self.port = 5003
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        # waiting client
        self.server_socket.listen(5)
        print('Server Socket is listening')
        # establish connection with client (conn: client socket, addr: binded address)
        self.conn, addr = self.server_socket.accept()
        print('Connected to :', addr[0], ':', addr[1])
        self.imgcnt = 1
        self.basename = "cam"

    def recvframe(self):

        # RECEIVE CAM FRAME
        while True:
            try:
                frame_data = self.server_socket.recv(4096)
                print("receiving frame...")
                if frame_data:
                    myfile = open('./camData/image%s.jpg' % self.imgcnt, 'wb')
                    myfile.write(frame_data)
                    frame_data = self.server_socket.recv(40960000)

                    if not frame_data:
                        myfile.close()
                        break
                    myfile.write(frame_data)
                    myfile.close()
                    self.server_socket.sendall("GOT IMAGE")
                    self.imgcnt += 1
            except:
                '''
                self.server_socket.close()
                self.conn.remove(sock)
                '''
                continue

        # server_socket.close()

    # Send_open/read file
    def sendcoordinates(self):
        while True:
            # read yolo_mark bounding box
            f = open("/home/heejunghong/BlackfencerWeb/index.html", 'r')
            data = f.read()
            self.conn.send(str(data))
            f.close()

    def shutdown(self):
        self.conn.close()
