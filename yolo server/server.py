import socket
import cv2
import numpy as np
import threading
import time
import random
import sys, os
sys.path.append(os.path.join(os.getcwd(), 'python/'))
sys.path.append(os.getcwd().replace('darknet', ''))
sys.path.append(os.getcwd().replace('darknet', 'temp_camNum/'))
sys.path.append(os.getcwd().replace('darknet', 'slice/'))


# server socket
host = "172.20.10.11"
port = 1234
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
# waiting client
sock.listen(2)
print('Server Socket is listening')
# establish connection with client (conn: client socket, addr: binded address) 
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
'''
def fileName():
    imgFileName = cam + in
'''
class Streaming(threading.Thread):
    def __init__(self):
        global conn
        threading.Thread.__init__(self)
        # stringData size (==(str(len(stringData))).encode().ljust(16))
        self.length = recvall(conn, 16)
        self.stringData = 1
        self.data = 1
        fileName_cnt = 0
        videoName_cnt = 0
        print("Streaming Thread Start")
        
    def run(self):
        global conn
        while True:
            print("############## run ############")
            # lock aquired by client
            # print_lock.acquire()
            '''
            # make cam img file
            recv_path = './temp_camNum'
            recv_fileList = os.listdir(recv_path)
            recv_fileList.remove(".DS_Store")
            if(fileName_cnt > 600):
                for fileName in recv_fileList:
                    os.sys("rm " + fileName)
                fileName_cnt = 0
            '''
            # recieve cam img
            stringData = recvall(conn, int(self.length))
            print('# get string_data')
            self.data = np.fromstring(stringData, dtype=np.uint8)
            print('## get self.data',self.data)
            # decoding data_streaming
            frame = cv2.imdecode(self.data, cv2.IMREAD_COLOR)
            print('### decode self.data')
            print("frame : ", frame)
            print("shape :", frame.shape)
            '''
            # store cam img
            img_fileName = fileName()
            print(img_fileName)
            
            if fileName_cnt
            
            # command: make mp4 file
            os.system("ffmpeg -f image2 -i temp_camNum/cam%4d.jpg data/media/"+videoName+".mp4")
            # command: run yolo
            os.system("./darknet detector demo data/obj.data cfg/yolov3.cfg backup/yolov3_3300.weights data/media/"+videoName+".mp4")
            '''
            # print(np.shape(frame))
            # show mp4
            cv2.imshow("viedo", frame)
            if cv2.waitKey(1) is 'q':
                break
            


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
