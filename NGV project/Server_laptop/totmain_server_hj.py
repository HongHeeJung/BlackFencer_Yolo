'''
2020.02.13.
raspberry pi to Yolo server: RECEIVE JUST ONE FRAME
'''
import cv2
import numpy as np
import threading
import time
import sys
import os
import socket
from socket import *

imgcnt = 1

def main():
    host = "192.168.255.21"
    port = 4000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((self.host, self.port))
    # waiting client
    server_socket.listen(5)
    print('Server Socket is listening')

    while
def threaded(client_socket, addr):
    print('Connected to :', addr[0], ':', addr[1])

class ReceiveImage(threading.Thread):
    def __init__(self):
        # server socket
        self.host = "192.168.255.21"
        self.port = 4000
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

    def run(self):

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

                # command: run yolo
                os.system(
                    './darknet detector test data/obj.data cfg/yolov3.cfg backup/yolov3_3300.weights '
                    'camData/image.jpg')

            except ValueError:
                print("no new frame")
                '''
                self.server_socket.close()
                self.conn.remove(sock)
                '''
                continue

        self.conn.close()
        print("Disconnect!")

    def shutdown(self):
        pass
        # server_socket.close()


class SendCoordinate(threading.Thread):
    def __init__(self):
        # server socket
        self.host = "192.168.255.21"
        self.port = 5000
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

    # Send_open/read file
    def run(self):
        while True:
            print("############## SC Run ####################")
            # read yolo_mark bounding box
            f = open("/home/heejunghong/BlackfencerWeb/index.html", 'r')
            data = f.read()
            self.conn.send(str(data))
            f.close()
            self.conn.close()

    def shutdown(self):
        pass


if __name__ == '__main__':
    print("### main start ###")
    main()

