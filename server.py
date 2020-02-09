from socket import *
import socket
import os
import time
import sys
import detector
import vvv

# image file path
src = "./temp"


def fileName():
    dte = time.localtime()
    Year = dte.tm_year
    Mon = dte.tm_mon
    Day = dte.tm_mday
    WDay = dte.tm_wday
    Hour = dte.tm_hour
    Min = dte.tm_min
    Sec = dte.tm_sec
    imgFileName = src + str(Year) + '_' + str(Mon) + '_' + str(Day) + '_' + str(Hour) + '_' + str(Min) + '_' + str(Sec)
    return imgFileName


# open server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.0.26", 1234))
server_socket.listen(5)

file_recive_cnt = 0

print("TCP Server Waiting for client on port 7163")

while True:

    # waiting client
    client_socket, address = server_socket.accept()
    # request successfully
    print("I got a connection from ", address)

    data = None

    # Data 수신
    while True:
        rev_path = './temp/'
        rev_flist = os.listdir(rec_path)
        rev_flist.remove(".DS_Store")
        if (file_recive_cnt > 2):
            for fname in rev_flist:
                os.sys("rm " + fname)
            file_recive_cnt = 0

        img_data = client_socket.recv(1024)
        data = img_data
        if img_data:
            while img_data:
                print("recving Img...")
                img_data = client_socket.recv(1024)
                data += img_data
            else:
                break

        # 받은 데이터 저장
        img_fileName = fileName()
        print(img_fileName)

        if file_recive_cnt == 0:
            img_fileName = img_fileName + ".mp4"
        elif file_recive_cnt == 1:
            img_fileName = img_fileName + '.txt'

        img_file = open(img_fileName, "wb")

        print("finish img recv")
        print(sys.getsizeof(data))

        img_file.write(data)
        img_file.close()
        client_socket.close()

        print("Finish ")
        file_recive_cnt += 1

        vvv.capture()  # 비디오 캡쳐.py
        detecor.detection()  # darknet.py

print("SOCKET closed... END")
