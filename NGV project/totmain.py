import cv2
import numpy as np
import threading
import time
import server
import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'python/'))
sys.path.append(os.getcwd().replace('darknet', ''))

imgcnt = 1

host = "192.168.255.21"
port = 4000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((self.host, self.port))
# waiting client
server_socket.listen(5)
print('Server Socket is listening')
# establish connection with client (conn: client socket, addr: binded address)
conn, addr = self.server_socket.accept()
print('Connected to :', addr[0], ':', addr[1])

img_cnt = 1

while True:
    try:
        frame_data = self.server_socket.recv(2048)
        print("receiving frame...")
        if frame_data:
            with open('./camData/*.jpg', 'wb') as my_file:
                my_file.write(frame_data)
                frame_data = server_socket.recv(2048)

            if not frame_data:
                my_file.close()
                break
            my_file.write(frame_data)
            my_file.close()
            server_socket.sendall("GOT IMAGE")

        # command: run yolo
        os.system(
            './darknet detector demo data/obj.data cfg/yolov3.cfg backup/yolov3_3300.weights '
            'camData/*.jpg')
        imgcnt += 1
        time.sleep(2)

        # read yolo_mark bounding box
        with open("/home/heejunghong/BlackfencerWeb/index.html", 'r') as my_file_2:
            data = my_file_2.read()
            conn.send(str(data))
            my_file_2.close()
        with open("/home/heejunghong/BlackfencerWeb/index.html", 'wt') as my_file_2:
            my_file_2.write('0')
            my_file_2.close()

    except Exception as ex:
        print('ERROR', ex)
        continue