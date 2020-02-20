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
#import detector
import shutil
import socket


def main():
    #rc = threading.Thread(target=recv_cam, args=(conn,))
    #rc.start()
    ry = threading.Thread(target=run_yolo, args=())
    ry.start()
    #sc = threading.Thread(target=send_coord, args=(conn,))
    #sc.start()

def run_yolo():               
    
    print("Analysis Initializing...")
    '''
    sys.path.append(os.path.join(os.getcwd(), 'python/'))
    print("PATH 1")
    import darknet as dn
    import pdb           
    print("Import successfully...")
          
    dn.set_gpu(0)
    net = dn.load_net("cfg/yolov3.cfg".encode('utf-8'), "backup/yolov3_3300.weights".encode('utf-8'), 0)
    meta = dn.load_meta("data/obj.data".encode('utf-8'))
                
    path = 'camtest/'
    file_list = os.listdir(path)   

    total_file_num = len(file_list)
    current_file_num = int()
    
    f = open('detection_result.txt', 'a')

    print("Start Analysis...")
    
    for current_file_num in range(1790):
        frame_name = "image{0:0>5}.jpg".format(current_file_num+500)
        print("Analysing..." + str(current_file_num) + '/' + str(total_file_num))
        frame_path = path + frame_name
        r = dn.detect(net, meta, frame_path.encode('utf-8'))
        
        current_file_num = current_file_num + 1
        print(str(current_file_num) + '///' + str(total_file_num))
        
        if r:
            print(frame_name, r)
            
            f.write(frame_name)
            f.write(str(r))
            f.write('\n')
    f.close()
    
    print("Analysing..." + str(current_file_num) + '/' + str(total_file_num))
    print("Analysing Finished!")               
    time.sleep(4)
    '''
    #except OSError:
    #except Exception as ex:
    #print('detector.py ERROR', ex)
    #break
    
    print("Darknet Faild to start!")
    print("Darknet Reinitializing...")
    '''
    if os.path.isfile("darknet/libdarknet.so"):
        os.remove("darknet/libdarknet.so")
    if os.path.isfile("darknet/libdarknet.a"):
        os.remove("darknet/libdarknet.a")
    if os.path.isfile("darknet/darknet"):
        os.remove("darknet/darknet")
    if os.path.isdir("darknet/obj/"):
        shutil.rmtree("darknet/obj/")
    '''
    #makepath = os.getcwd() + "/darknet"
    makepath = os.getcwd()
    os.system("make -C " + makepath)

    print("Darknet Reinitializing Finished")
    print("Please try again Analysis")
           
'''
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


def recv_cam(sock):
    global conn
    while True:
        recv_path = 'camData/'
        with open('./camData/'+frame_name, 'wb') as my_file:
            print("Hello")
            length = recvall(conn, 16)
            print("Bye")
            frame_data = recvall(conn, int(length))
            print("receiving frame...")
            time.sleep(1)
            while frame_data:
                cv2.imwrite("./camData/"+ str(int(index/3)) + ".jpg", frame_data)
                print("Now frame Updated!")
            else:
                break
    

def send_coord(sock):
    global conn
    while True:
        print("waiting....")
        time.sleep(4)
        # read yolo_mark bounding box
        with open("/home/heejunghong/BlackfencerWeb/index.html", 'r') as my_file_2:
            data = my_file_2.read()
            print("Read the bounding box's coordinate")
            conn.send(data)
            print("Send bounding box's coordinate successfully!")
            time.sleep(2)
        with open("/home/heejunghong/BlackfencerWeb/index.html", 'w') as my_file_2:     
            my_file_2.write('0')
            print("Initialize the bounding box's coordinate to 0")
            # my_file_2.close()
'''
'''
host = "192.168.0.122"
port = 4000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
# waiting client
server_socket.listen(5)
print('Server Socket is listening')
# create_thread(server_socket)

# establish connection with client (conn: client socket, addr: binded address)
conn, addr = server_socket.accept()
print('Connected to :', addr[0], ':', addr[1])
# server_socket.close()
'''
if __name__ == '__main__':
    main()
    print('end')
