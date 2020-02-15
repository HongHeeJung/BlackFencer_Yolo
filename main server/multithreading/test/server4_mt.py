import socket
import cv2
import numpy as np
import threading
import time
import random


# server IP
host = "192.168.35.12"
port = 1234
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((host, port))
# waiting client
server_sock.listen(2)
print('Socket is listening')
# establish connection with client (conn: socket, addr: binded address) 
conn, addr = sock.accept()
print('Connected to :', addr[0], ':', addr[1])


def main():
    mystreaming = Streaming()
    mystreaming.start()
    mysendcoords = SendCoordinates()
    mysendcoords.start()


# Streaming_return buffer
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


class Streaming(threading.Thread):
    def __init__(self):
        global conn
        threading.Thread.__init__(self)
        # stringData size (==(str(len(stringData))).encode().ljust(16))
        self.length = recvall(conn, 16)
        self.data = np.zeros(0)

    def run(self):
        global conn
        while True:
            # lock aquired by client
            # print_lock.acquire()
            string_data = recvall(conn, int(self.length))
            print('##')
            self.data = np.fromstring(string_data, dtype=np.uint8)
            print('###')
            # decoding data_streaming
            frame = cv2.imdecode(self.data, cv2.IMREAD_COLOR)
            # print(np.shape(frame))
            cv2.imshow('ImageWindow', frame)
            cv2.waitKey(1)


# Send_open/read file
class SendCoordinates(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.data = np.zeros(0)

    def run(self):
        global conn
        while True:
            time.sleep(0.1)
            # client2_yolo_mark bounding box
            f = open("/home/heejunghong/BlackfencerWeb/index.html", 'r')
            self.data = f.read()
            conn.send(str(self.data))
            f.close()


if __name__ == '__main__':
    main()



