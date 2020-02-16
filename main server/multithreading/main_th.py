'''
2020.02.13.
'''
# coding=<ascii>
import cv2
import numpy as np
import threading
import time
import socket
import sys
import os
import detector

host = "192.168.255.21"
port = 4000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
# waiting client
server_socket.listen(5)
print('Server Socket is listening')


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


def telecommunication():
    global server_socket
    while True:
        # establish connection with client (conn: client socket, addr: binded address)
        conn, addr = server_socket.accept()
        print('Connected to :', addr[0], ':', addr[1])
        try:
            with open('./camData/image.jpg', 'wb') as my_file:
                length = recvall(conn, 16)
                frame_data = recvall(conn, int(length))
                print("receiving frame...")
                my_file.write(frame_data)
                print("Now frame Updated!")
                my_file.close()

            time.sleep(4)

            # read yolo_mark bounding box
            with open("/home/heejunghong/BlackfencerWeb/index.html", 'r+w') as my_file_2:
                data = my_file_2.read()
                print("Read the bounding box's coordinate...")
                conn.send(data)
                print("Send bounding box's coordinate successfully!")
                time.sleep(2)
                my_file_2.write('0')
                my_file_2.close()
                print("Initialize the bounding box's coordinate to 0")
            continue

        except Exception as ex:
            print('ERROR', ex)
            break


def runyolo():
    # command: run yolo
    myrunyolo = RunYolo()
    myeunyolo.start()
    if myrunyolo.is_alive() is True:
        thread.exit()


if __name__ == '__main__':
    telecommunication()
    thread.start_new_thread(runyolo, ())
    print('end')