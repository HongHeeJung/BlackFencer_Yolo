import socket
import cv2
import numpy as np
# import requests
#import _thread
import threading
import thread
from thread import *
import time
import random

 
# Streaming_return buffer
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        #buf = newbuf
        count -= len(newbuf)
    return buf   
    

# Send_open/read file
def sendcord():

    #client2_yolo_mark bounding box 
    f = open("/home/heejunghong/BlackfencerWeb/index.html", 'r')
    data = f.read()
    conn.send(str(data))
    f.close()

# Connect
#def connect():
# localhost IP
host = "192.168.35.12"
port = 8888
 
# Create TCP Socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host, port))
# put the socket into listening mode_waiting client
sock.listen(2)
print('Socket is listening')
# establish connection with client (conn: socket, addr: binded address) 
conn,addr = sock.accept() 

while True:
    # lock aquired by client
    # print_lock.acquire()
    # print('Connected to :', addr[0], ':', addr[1])
                    
    #stringData size (==(str(len(stringData))).encode().ljust(16))
    length = recvall(conn, 16)
    print('#')
    stringData = recvall(conn, int(length))
    print('##')
    data = np.fromstring(stringData, dtype = np.uint8)
    print('###')
        
    # client1_decoding data_streaming
    frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
    # print(np.shape(frame))
    cv2.imshow('ImageWindow',frame)
    cv2.waitKey(1) 


if __name__== '__main__':
    #connect()
    # for i in range(10000):
    # thread.start_new_thread(recvall)
    # thread.start_new_thread(sendcord)
    print('STOP?')
    #thread1 = threading.Thread(recvall, args=(i))
    '''
    thread1 = threading.Thread(recvall, (sock, count))
    thread1.start()   
    thread2 = threading.Thread(sendcord)
    thread2.start()        
    '''    

