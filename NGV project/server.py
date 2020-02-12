from socket import *
import socket
import cv2
import numpy as np
import time
import sys
import os

# sys.path.append(os.path.join(os.getcwd(), 'python/'))
# sys.path.append(os.getcwd().replace('darknet', ''))
# sys.path.append(os.getcwd().replace('darknet', 'camData/'))
# sys.path.append(os.getcwd().replace('darknet', 'img1/'))


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


class Telecommunication(self):
    def __init__(self):
        # server socket
        self.host = "192.168.255.21"
        self.port = 5003
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        # waiting client
        server_socket.listen(5)
        print('Server Socket is listening')
        # establish connection with client (conn: client socket, addr: binded address)
        self.conn, self.addr = server_socket.accept()
        print('Connected to :', addr[0], ':', addr[1])

    def recvframe(self):

        for _ in range(1):
            data = None
            # RECEIVE CAM FRAME
            while True:
                print("############## receive cam frame ###############")
                '''
                # delete the used frames
                rev_path = './camData/'
                rev_frame_list = os.listdir(rev_path)
                if ".USED" in rev_frame_list:
                    rev_frame_list.remove(".USED")
                '''
                frame_data = self.conn.recv(1000000)
                data = frame_data

                if frame_data:
                    while frame_data:
                        print("receiving frames...")
                        frame_data = conn.recv(1000000)
                        data += frame_data
                        print(len(data))
                        time.sleep(1)
                    else:
                        break

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