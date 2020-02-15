'''
2020.02.13.
2020.02.15. - rpi: Server /laptop(yolo): Client
'''
# coding=<ascii>
import cv2
import numpy as np
# import threading
import time
import socket
import sys
import os
import detector
import multiprocessing


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


class DetectFrame(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.exit = multiprocessing.Event()
        self.host = "192.168.255.21"
        self.port = 4000

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        # waiting client
        self.server_socket.listen(5)
        print('Server Socket is listening')

    def run(self):
        while not self.exit.is_set():
            # establish connection with client (conn: client socket, addr: binded address)
            conn, addr = self.server_socket.accept()
            print("++++++++++++++++++++++++++++++ CONNECTED +++++++++++++++++++++++++")
            print('Connected to :', addr[0], ':', addr[1])
            try:
                with open('./camData/image.jpg', 'wb') as my_file:
                    length = recvall(conn, 16)
                    frame_data = recvall(conn, int(length))
                    print("receiving frame...")
                    my_file.write(frame_data)
                    print("Now frame Updated!")
                    my_file.close()

                # command: run yolo
                myRunYolo = detector.RunYolo()
                if not myRunYolo.is_alive():
                    print("[Thread]: Run Yolo")
                    myRunYolo.start()
                    del myRunYolo
                else:
                    del myRunYolo
                    time.sleep(1)

                # read yolo_mark bounding box
                with open("/home/heejunghong/BlackfencerWeb/index.html", 'w+t') as my_file_2:
                    data = my_file_2.read()
                    print("Read the bounding box's coordinate")
                    conn.send(data)
                    print("Send bounding box's coordinate successfully!")
                    time.sleep(2)
                    my_file_2.write('0')
                    print("Initialize the bounding box's coordinate to 0")
                    my_file_2.close()

            except Exception as ex:
                print('main.py ERROR', ex)
                break

            # conn.close()
            # self.server_socket.close()
            # print("++++++++++++++++++++++++++++ DISCONNECTED +++++++++++++++++++++++")

    def shutdown(self):
        print("Shutdown initiated")
        self.exit.set()


if __name__ == '__main__':
    myDetectFrame = DetectFrame()
    myDetectFrame.start()
    print("processing start 1")
    myDetectFrame.shutdown()
    time.sleep(1)
    while True:
        if not myDetectFrame.is_alive():
            myDetectFrame.start()
            myDetectFrame.shutdown()
        else:
            break