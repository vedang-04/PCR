import glob
import json
# import cv2
import fiftyone as fo
import numpy

ff = {}
list_of_files = glob.glob(r'C:\Users\kshir\OneDrive\Desktop\PCR-master\MSRA-TD500\test\*.gt')
list_of_files_seg = glob.glob(r'C:\Users\kshir\OneDrive\Desktop\PCR-master\MSRA-TD500\test\*.txt')

list_of_images = glob.glob(r'C:\Users\kshir\OneDrive\Desktop\PCR-master\MSRA-TD500\test\*.jpg')

print(len(list_of_files))

for f in range(len(list_of_files)):
    file = open(list_of_files[f], 'r')
    file1 = open(list_of_files_seg[f], 'r')
    t = file.readlines()
    t1 = file1.readlines()
    lff=[]
    for i in range(len(t)):
        l = t[i].split('\n')[0]
        lf = l.split(',')
        lf.append(t1[i].split('\n')[0].split(',')[-1])
        lff.append(' '.join(lf))
    file2 = open(r'C:\Users\kshir\OneDrive\Desktop\PCR-master\det_f'+'\\'+list_of_files_seg[f].split('\\')[-1], "w")
    file2.write('\n'.join(lff)+'\n')

print("DONE")