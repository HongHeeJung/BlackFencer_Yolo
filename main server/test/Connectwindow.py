import cv2
import numpy as np
import threading
import socket
import os, sys, time
import shutil
# function code
import serversock,  DataRecv


class ConnectWindow(Connect):
    def __init__(self, w2):
        self.IP = "192.168.255.21"
        self.Port = "5000"
        self.workingFlag = 0
        self.successFlag = 0

        self.ConnectThread = DataRecvThread()

        Connect.__init__(self)
        self.connectButton.clicked.connect(self.RecvData)
        self.cancelButton.clicked.connect(self.CancelProcess)

    def RecvData(self):
        flist = os.listdir("slice/")
        for f in flist2:
            os.remove("slice/" + f)

        self.ConnectThread.IP = self.IP
        self.ConnectThread.Port = self.Port
        self.ConnectThread.start()

    def CancelProcess(self):
        if self.ConnectThread.workingFlag == 0:
            self.Dialog.close()
        elif self.ConnectThread.workingFlag == 1:
            self.connectLog(6)

    def connectLog(self, flag):
        if flag == 1:
            self.workingFlag = 1
            self.loglabel.setText("Receiving file...")
        elif flag == 2:
            self.workingFlag = 0
            self.loglabel.setText("Data Receive Success!")
        elif flag == 3:
            self.loglabel.setText("Timeout! Please Reconnect.")
        elif flag == 4:
            self.loglabel.setText("Data Receive Fail...")
        elif flag == 5:
            self.loglabel.setText("Data Receiving now... Please Wait.")
        elif flag == 6:
            self.successFlag = 1 # receive success
        elif flag == 7:
            self.successFlag = 2 # receive fail