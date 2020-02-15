from socket import *
import socket
import os
import time
import sys
import preprocess


def fileName():
    # 이미지 파일 저장경로
    src = "../temp/"

    dte = time.localtime()
    Year = dte.tm_year
    Mon = dte.tm_mon
    Day = dte.tm_mday
    WDay = dte.tm_wday
    Hour = dte.tm_hour
    Min = dte.tm_min
    Sec = dte.tm_sec
    imgFileName = src + str(Year) + '-' + str(Mon) + '-' + str(Day) + '_' + str(Hour) + ':' + str(Min) + ':' + str(Sec)
    return imgFileName


def so(IP, Port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, int(Port)))
    server_socket.listen(5)

    file_recive_cnt = 0

    print("TCPServer Waiting for client on port " + str(Port))
    # print(os.getcwd())

    for _ in range(2):

        # 클라이언트 요청 대기중 .
        client_socket, address = server_socket.accept()
        # 연결 요청 성공
        print("I got a connection from ", address)

        data = None

        # RECEIVE FRAME
        while True:
            rev_path = 'camData/'
            rev_flist = os.listdir(rev_path)
            if ".DS_Store" in rev_flist:
                rev_flist.remove(".DS_Store")

            # if len(rev_flist) >= 2:
            #     for fname in rev_flist:
            #         os.system('rm ' + 'temp/' + fname)
            #         # subprocess.call('rm ' + 'temp/'+fname, shell=True)
            #     file_recive_cnt = 0

            img_data = client_socket.recv(1000000)
            data = img_data

            if img_data:
                while img_data:
                    print("recving Img...")
                    img_data = client_socket.recv(1000000)
                    data += img_data
                    print(len(data))
                else:
                    break

        # SAVE FRAME
        img_fileName = fileName()
        print(img_fileName)

        if file_recive_cnt == 0:
            img_fileName = img_fileName+".mp4"
        elif file_recive_cnt == 1:
            img_fileName = img_fileName+'.txt'

        img_file = open("temp/"+img_fileName, "wb")

        print("finish img recv")
        print(sys.getsizeof(data))

        img_file.write(data)
        img_file.close()
        client_socket.close()

        print("Finish ")

        data = None
        file_recive_cnt += 1