'''
2020.02.13.
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import threading
import time
import socket
import sys
import os
import detector
import shutil
import socket


# command: run yolo
# if runyolo_ctrl == 1:
'''
myRunYolo = RunYolo()
if runyolo_ctrl == 1:
    print(myrunyolo_ctrl)
    myRunYolo.start()
    del myRunYolo
    myRunYolo.exit()
    runyolo_ctrl = 0
'''
def main():
    rc = threading.Thread(target=recv_cam, args=(conn,))
    rc.start()
    myRunYolo = RunYolo()
    myRunYolo.start()
    myRunYolo.exit()
    sc = threading.Thread(target=send_coord, args=(conn,))
    sc.start()


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


def recv_cam(sock):
    while True:
        print(self.conn)
        with open('./camData/image.jpg', 'wb') as my_file:
            print("Hello")
            length = recvall(self.conn, 16)
            print("Bye")
            frame_data = recvall(self.conn, int(length))
            print("receiving frame...")
            my_file.write(frame_data)
            print("Now frame Updated!")


def send_coord(sock):
    while True:
        print("waiting....")
        time.sleep(4)
        # read yolo_mark bounding box
        with open("/home/heejunghong/BlackfencerWeb/index.html", 'w+t') as my_file_2:
            data = my_file_2.read()
            print("Read the bounding box's coordinate")
            self.conn.send(data)
            print("Send bounding box's coordinate successfully!")
            time.sleep(2)
            my_file_2.write('0')
            print("Initialize the bounding box's coordinate to 0")
            # my_file_2.close()

'''
class Cserver(threading.Thread):
    def __init__(self, socket):
        super().__init__()
        self.server_socket = socket

    def run(self):
        # global runyolo_ctrl
        global index
        

        index = index+1
        create_thread(self.server_socket)
        t=threading.Thread(target=self.conn)
        t.deamon=True
        t.start()

    def shutdown(self):
        print("Shutdown initiated")
        self.exit.set()


def create_thread(server_socket):
    global index
    t.append(Cserver(server_socket))
    t[index].deamon=True
    t[index].start()
'''

# t = []
index = 0

host = "192.168.255.21"
port = 4000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
# waiting client
server_socket.listen(5)
print('Server Socket is listening')
create_thread(server_socket)

# establish connection with client (conn: client socket, addr: binded address)
conn, addr = self.server_socket.accept()
print('Connected to :', addr[0], ':', addr[1])
# server_socket.close()

if __name__ == '__main__':
    main()
    print('end')

