import sys, os

sys.path.append(os.path.join(os.getcwd(), 'python/'))
sys.path.append(os.getcwd().replace('darknet', ''))
sys.path.append(os.getcwd().replace('darknet', 'temp/'))
sys.path.append(os.getcwd().replace('darknet', 'slice/'))
import darknet as dn
import pdb

dn.set_gpu(0)
net = dn.load_net("cfg/yolov3.cfg".encode('utf-8'), "backup_corn/yolov3_34000.weights".encode('utf-8'), 0)
meta = dn.load_meta("cfg/coco.data".encode('utf-8'))

path = '../slice/'
file_list = os.listdir(path)
if ".DS_Store" in file_list:
    file_list.remove(".DS_Store")

total_file_num = len(file_list)
current_file_num = int()

f = open('../detection_result.txt', 'a')

for file_name in file_list:
    filepath = path + file_name
    r = dn.detect(net, meta, filepath.encode('utf-8'))

    current_file_num = current_file_num + 1
    print(str(current_file_num) + '///' + str(total_file_num))

    if r:
        print(r)
        print(file_name)

        with open('../detection_result.txt', 'a') as fileobject:
            fileobject.write(file_name)
            fileobject.write('\n')

print("END")