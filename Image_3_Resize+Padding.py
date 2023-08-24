import os
import cv2

BF = r'BF0'
BW = r'BW0'
WF = r'WF0'
WW = r'WW0'

BFT = BF + '\\' + 'T'
BWT = BW + '\\' + 'T'
WFT = WF + '\\' + 'T'
WWT = WW + '\\' + 'T'

names = os.listdir(BFT)
for name in names:
    iT = BFT + '\\' + name
    
    imgT = cv2.imread(iT)
    h,w = imgT.shape[:2]
    imgT = cv2.resize(imgT,(int(1.2*w),int(1.2*h)),interpolation=cv2.INTER_CUBIC)
    if(h>120):
        h = 120
    if(w>120):
        w = 120
    imgT = cv2.resize(imgT,(w,h),interpolation=cv2.INTER_CUBIC)
    hx = 120 - h
    wx = 120 - w
    hx = int(hx/2)
    wx = int(wx/2)
    #print(imgT.shape)
    imgT = cv2.copyMakeBorder(imgT, hx, hx, wx, wx, cv2.BORDER_CONSTANT, value=(0,0,0))
    #print(imgT.shape)
    imgT = cv2.resize(imgT,(120,120),interpolation=cv2.INTER_CUBIC)
    #print(imgT.shape)
    OUT = iT
    cv2.imwrite(OUT,imgT)
    
names = os.listdir(BWT)
for name in names:
    iT = BWT + '\\' + name


    imgT = cv2.imread(iT)
    h,w = imgT.shape[:2]
    if(h>120):
        h = 120
    if(w>120):
        w = 120
    imgT = cv2.resize(imgT,(w,h),interpolation=cv2.INTER_CUBIC)
    hx = 120 - h
    wx = 120 - w
    hx = int(hx/2)
    wx = int(wx/2)
    #print(imgT.shape)
    imgT = cv2.copyMakeBorder(imgT, hx, hx, wx, wx, cv2.BORDER_CONSTANT, value=(0,0,0))
    #print(imgT.shape)
    imgT = cv2.resize(imgT,(120,120),interpolation=cv2.INTER_CUBIC)
    #print(imgT.shape)
    OUT = iT
    cv2.imwrite(OUT,imgT)
    
names = os.listdir(WFT)
for name in names:
    iT = WFT + '\\' + name


    imgT = cv2.imread(iT)
    h,w = imgT.shape[:2]
    if(h>120):
        h = 120
    if(w>120):
        w = 120
    imgT = cv2.resize(imgT,(w,h),interpolation=cv2.INTER_CUBIC)
    hx = 120 - h
    wx = 120 - w
    hx = int(hx/2)
    wx = int(wx/2)
    #print(imgT.shape)
    imgT = cv2.copyMakeBorder(imgT, hx, hx, wx, wx, cv2.BORDER_CONSTANT, value=(0,0,0))
    #print(imgT.shape)
    imgT = cv2.resize(imgT,(120,120),interpolation=cv2.INTER_CUBIC)
    #print(imgT.shape)
    OUT = iT
    cv2.imwrite(OUT,imgT)
    
names = os.listdir(WWT)
for name in names:
    iT = WWT + '\\' + name


    imgT = cv2.imread(iT)
    h,w = imgT.shape[:2]
    if(h>120):
        h = 120
    if(w>120):
        w = 120
    imgT = cv2.resize(imgT,(w,h),interpolation=cv2.INTER_CUBIC)
    hx = 120 - h
    wx = 120 - w
    hx = int(hx/2)
    wx = int(wx/2)
    #print(imgT.shape)
    imgT = cv2.copyMakeBorder(imgT, hx, hx, wx, wx, cv2.BORDER_CONSTANT, value=(0,0,0))
    #print(imgT.shape)
    imgT = cv2.resize(imgT,(120,120),interpolation=cv2.INTER_CUBIC)
    #print(imgT.shape)
    OUT = iT
    cv2.imwrite(OUT,imgT)