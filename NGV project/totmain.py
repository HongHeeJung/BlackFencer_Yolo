import cv2
import numpy as np
import threading
import time
import socket
import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'python/'))
sys.path.append(os.getcwd().replace('darknet', ''))

imgcnt = 1

host = "192.168.255.21"
port = 4000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
# waiting client
server_socket.listen(5)
print('Server Socket is listening')

img_cnt = 1

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def runyolo(a):
    with open("/home/heejunghong/BlackfencerWeb/index.html", 'wt') as my_file_2:
        print("html reset")
        my_file_2.write('0')
        my_file_2.close()
    os.system(
            './darknet detector demo data/obj.data cfg/yolov3.cfg backup/yolov3_3300.weights '
            'camData/*.jpg')
        imgcnt += 1
        time.sleep(2)

while True:
    # establish connection with client (conn: client socket, addr: binded address)
    conn, addr = server_socket.accept()
    print('Connected to :', addr[0], ':', addr[1])
    try:
        length = recvall(conn,16)
        frame_data = recvall(conn, int(length))
        
        if frame_data:
            print("receiving frame...")
            with open('./camData/*.jpg', 'wb') as my_file:
                my_file.write(frame_data)
                print("frame Update!")                
                my_file.close()
        else:
            break
        
        # command: run yolo
        rn = threading.Thread(target = runyolo, args = (1, ))
        rn.start()

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

if __name__ == '__main__':
    main()
    print('end')   
