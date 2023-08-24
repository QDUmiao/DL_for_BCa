import os
import SimpleITK as sitk
import numpy as np
import math
import pandas as pd
pc1 = 0 
pc2 = 0.998

ERROR = []
def scale(image_path,out):
    global ERROR
    image = sitk.ReadImage(image_path)
    image_array = sitk.GetArrayFromImage(image)
    imgArray = np.float32(image_array) + 0
    
    imgPixel = imgArray[imgArray >= 0]
    print(imgPixel.shape)
    imgPixel.sort()
    print(imgPixel)
    
    m1 = imgPixel[0]
    m2 = imgPixel[len(imgPixel)-1]
    
    index = int(round(len(imgPixel) - 1) * pc1 + 0.5)
    if index < 0:
        index = 0
    if index > (len(imgPixel) - 1):
        index = len(imgPixel) - 1
    p1 = imgPixel[index]
    
    
    index = int(round(len(imgPixel) - 1) * pc2 + 0.5)
    if index < 0:
        index = 0
    if index > (len(imgPixel) - 1):
        index = len(imgPixel) - 1
    p2 = imgPixel[index]
    print("新边界值",p1,p2)
    
    # imgPixel2 = np.clip(imgPixel,p1,p2)

    u50 = np.median(imgPixel)
    print("中值",u50)
    
    s1 = 0
    s2 = 4095
    usg = s1
    
   
    if(p1 - u50 == 0):
        ERROR.append(image_path)
        pd.DataFrame(columns=['PATH'],data=ERROR).to_csv(r'ERRORRR.csv',encoding='utf_8_sig')
        u50 = p1 + 1
        for i in range(imgArray.shape[0]):
            for j in range(imgArray.shape[1]):
                for k in range(imgArray.shape[2]):
                    #print(i,j,k)
                    x = imgArray[i][j][k]
                    if(x >= m1 and x <= u50):
                        imgArray[i][j][k] = math.ceil(usg +(x - u50)*(s1 - usg)/(p1 - u50))
                    elif(x >= u50 and x <= m2):
                        imgArray[i][j][k] = math.ceil(usg +(x - u50)*(s2 - usg)/(p2 - u50))
        img = sitk.GetImageFromArray(imgArray, isVector=False)
        sitk.WriteImage(img,out)
        
    elif(p2 - u50 == 0):
        ERROR.append(image_path)
        pd.DataFrame(columns=['PATH'],data=ERROR).to_csv(r'ERRORRR.csv',encoding='utf_8_sig')
        u50 = p2 - 1
        for i in range(imgArray.shape[0]):
            for j in range(imgArray.shape[1]):
                for k in range(imgArray.shape[2]):
                    #print(i,j,k)
                    x = imgArray[i][j][k]
                    if(x >= m1 and x <= u50):
                        imgArray[i][j][k] = math.ceil(usg +(x - u50)*(s1 - usg)/(p1 - u50))
                    elif(x >= u50 and x <= m2):
                        imgArray[i][j][k] = math.ceil(usg +(x - u50)*(s2 - usg)/(p2 - u50))
                        
        img = sitk.GetImageFromArray(imgArray, isVector=False)
        sitk.WriteImage(img,out)
        
    else:
        for i in range(imgArray.shape[0]):
            for j in range(imgArray.shape[1]):
                for k in range(imgArray.shape[2]):
                    #print(i,j,k)
                    x = imgArray[i][j][k]
                    if(x >= m1 and x <= u50):
                        imgArray[i][j][k] = math.ceil(usg +(x - u50)*(s1 - usg)/(p1 - u50))
                    elif(x >= u50 and x <= m2):
                        imgArray[i][j][k] = math.ceil(usg +(x - u50)*(s2 - usg)/(p2 - u50))
    
        img = sitk.GetImageFromArray(imgArray, isVector=False)
        sitk.WriteImage(img,out)


path = r'T'
OUT = r'OUT'
names = os.listdir(path)
count = 0
size = len(names)
for name in names:
    image_path = path + '\\' + name
    out = OUT + '\\' + name
    scale(image_path,out)
    count += 1
    print(str(round(count*100/size)) + "%")