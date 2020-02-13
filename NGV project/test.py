import cv2
import numpy as np
import threading
import time
import server
import sys
import os
from socket import *
from select import *
from image import *
from coordinate import *
# sys.path.append(os.path.join(os.getcwd(), 'python/'))
# sys.path.append(os.getcwd().replace('darknet', ''))

imgcnt = 1

# server socket
host = "192.168.255.21"
port = 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((self.host, self.port))
# waiting client
server_socket.listen(5)
connection_list = [server_socket]
print("#"*50)
print("[Thread version] init Server Socket successfully")
print("[info] Server Socket is listening")
print("#"*50)

while connection_list:
    try:
        readSock, writeSock, errorSock = select(connection_list, [], [], 5)
        for sock in readSock:
            if sock == server_socket:
                client_socket, addr = server_socket.accept()

    except Keyboardinterrupt:
        server_socket.close()
        sys.exit()

# establish connection with client (conn: client socket, addr: binded address)
self.conn, addr = self.server_socket.accept()
print('Connected to :', addr[0], ':', addr[1])
self.imgcnt = 1
self.basename = "cam"

def main():
    ts = server.Telecommunication()
    while True:
        ts.recvframe()
        runYolo()
        time.sleep(4)
        ts.sendcoordinates()


def runYolo():
    global imgcnt
    # command: run yolo
    os.system(
        './darknet detector demo data/obj.data cfg/yolov3.cfg backup/yolov3_3300.weights '
        'camData/image%s.jpg' % imgcnt)
    imgcnt += 1


if __name__ == '__main__':
    print("### main start ###")
    main()
