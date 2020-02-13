import cv2
import os


def capture():
    videopath = 'temp/'
    filelist = os.listdir(videopath)
    if ".DS_Store" in filelist:
        filelist.remove(".DS_Store")

    for fname in filelist:
        if ".mp4" in fname:
            videoname = fname
    video = cv2.VideoCapture(videopath + videoname)

    temp = int()
    index = int()
    result_frame_list = list()

    if not os.path.isdir("slice/"):
        os.mkdir("slice/")

    while (video.isOpened()):
        ret, frame = video.read()
        print(ret)
        if index % 3 == 0:
            result_frame_list.append(frame)
            cv2.imwrite("slice/" + str(int(index / 3)) + ".jpg", frame)

        if ret == True:
            temp = temp + 1
            index = index + 1

        if ret == False:
            break;
    video.release()
    print(temp)