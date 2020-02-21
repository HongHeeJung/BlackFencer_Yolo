# -*- coding: utf-8 -*- 
import cv2
import numpy as np
import threading
import io
import socket
import sys
import struct
import time
import pickle
import zlib
import os
import shutil


# input server socket
host = "192.168.0.116"
port = 4000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print("Connected")


def main():
    # socket
    sc = threading.Thread(target=send_coord, args=(client_socket,))
    sc.start()
   

def send_coord(sock):
    global conn
    while True:
        print("waiting....")
        time.sleep(4)
        # read yolo_mark bounding box   
        with open("/home/heejunghong/BlackfencerWeb/index.html", 'r') as my_file_2:
            data = my_file_2.read()
            print("Read the bounding box's coordinate")
            #_data = str(data).replace('я', '')
            _data = data.strip()
            print("_data " ,_data)
            
            #client_socket.sendall((str(len(_data))).ljust(16) + _data)
            client_socket.sendall(_data)
            
            print("Send bounding box's coordinate successfully!")
            my_file_2.close()
            time.sleep(2)



if __name__ == '__main__':
    main()
