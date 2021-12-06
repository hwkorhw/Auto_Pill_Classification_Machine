import numpy as np
import cv2 as cv
#from readcsv import r
import time
import sys
from stepm import final_i
#from PyQt5 import QtCore, QtGui, QtWidgets

# innit net
tensorflowNet = cv.dnn.readNet('frozen_graph_EB0_for_dnn.pb')

if tensorflowNet is not None:
    print('---Net is ready---')
else:
    print('---Net error---')
    sys.exit()
    
    
erode_count=2
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
cX=365
cY=430
c2X=cX+850
c2Y=cY+20
r1=240 #220 too small # 240 하면 38클래스에서 짤림
r2=r1

def show_info(self, i, num):
        self.MainD = QtWidgets.QDialog()
        self.detail_info = pill_ui2.Ui_MainWindow(self.MainD)
        self.detail_info.show_ui(i, num)
        self.MainD.show()
        
def pre_proc(frame_up, frame_down): #공통된 전처리
    image = np.hstack((frame_up, frame_down))

    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    (h, w) = image.shape[:2]
    mask = np.zeros(gray.shape,dtype=np.uint8)
    mask2= image.copy()
    m = np.zeros(gray.shape,dtype=np.uint8)
    cv.circle(mask, (cX,cY), r1, (255, 255, 255), -1)
    cv.circle(mask2, (cX,cY), r1, (0, 0, 0), -1)
    cv.circle(mask2, (c2X,c2Y), r2, (0, 0, 0), -1)
    cv.circle(m, (c2X,c2Y), r2, (255, 255, 255), -1)

    dst = cv.bitwise_and(image,image,None,mask)
    dst2 = cv.bitwise_and(image,image,None,m)

    crop1 = dst[cY-r1:cY+r1,cX-r1:cX+r1]
    crop2 = dst2[c2Y-r2:c2Y+r2,c2X-r2:c2X+r2]
    full = np.hstack((crop1,crop2))

    for z in range(erode_count):
        full = cv.erode(full, kernel)

    return full


def infer(frame_up, frame_down):
    #start_time = time.time()
    net_input = pre_proc(frame_up, frame_down)
    copy = net_input.copy()
    net_input = cv.dnn.blobFromImage(net_input, 1/255, size=(224,224), swapRB=True)
   # print(net_input.shape)
    tensorflowNet.setInput(net_input) # 1 3 224 224 # NCHW  #swapRB=True, crop=False
    #print(net_input.shape)
    pre_time = time.time()
    
    networkOutput = tensorflowNet.forward()
    end_time = time.time()
    
    idx = np.argmax(networkOutput) # pill index
    print(idx)
    
    #pn = r[idx][1] # pill name
    #pg = r[idx][5] # pill guide 0 1 2
    #print(idx, pn, pg)
    #return pn, pg    
    # print(idx, 'pre_time={:.3f} s'.format((pre_time -start_time)),
    #      'infer_time={:.3f} s'.format((end_time -pre_time))
    #      )
    return idx, copy
