from Connectwindow import Connect # Connectwindow ui 코드
import cv2
import numpy as np
import threading
import socket
import os, sys, time
import shutil
# function code
import serversock, detector, DataRecv


# SUPER CLASS
class Main:
    def __init__(self, w):
        self.framepath = "camData/"
        ConnectThread = DataRecvThread()
        ConnectThread.start()
        self.AnalysisThread = darknet()

        Ui_Mainwindow.__init__(self)
        self.setupUi(w)
        self.initButton.clicked.connect(self.InitData)
        self.recvButton.clicked.connect(self.DataReceive)
        self.analButton.clicked.connect(self.DataAnalysis)

    # Cache Clear
    def InitData(self):
        self.logBrowser.append("Cache Initialize Start...")
        if os.path.isdir(self.framepath):
            filelist = os.listdir(self.framepath)

            for file in filelist:
                os.remove(self.framepath + file)
        else:
            self.logBrowser.append("Cache Folder not exist!!")
            os.mkdir(self.framepath)
            self.logBrowser.append("Created Cache Folder!")

        self.logBrowser.append("Cache Initialize Finished")

    # Data Analysis
    def DataAnalysis(self):
        if self.AnalysisThread.workingFlag == 0:
            self.AnalysisThread.start()
        else:
            print("wait...")

    # Data Receive
    def DataReceive(self):
        run_connect = ConnectWindow(w2)
        run_connect.exec_()

        if ui.successFlag == 1:
            self.logPrint("Data Receive Success!")
        elif ui.successFlag == 2:
            self.logPrint("Data Receive Fail...")


class DataRecvThread(threading.Thread):
    def __init__(self):
        self.IP = "192.168.255.21"
        self.Port = "5000"
        self.workingFlag = 0

    def run(self):
        while True:
            try:
                # 진행상황을 메시지로 전송하며 진행
                self.workingFlag = 1
                self.connectState.emit(1)
                # execute telecommunication
                server.so(self.IP, int(self.Port))
                self.workingFlag = 0

            except Exception as ex:
                print('ERROR', ex)
                time.sleep(3)
                self.workingFlag = 0
                continue

if __name__ == "__main__":
    run_main = Main(w)
    print("END")