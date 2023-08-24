import numpy as np
import imageio
import os
import cv2
import shutil
import nibabel as nib

def MaxROI(di,outpath):
    length = 0
    width = 0
    mid = []
    midname = []
    picname = []
    names = os.listdir(di)
    for name in names:
        names2 = os.listdir(di + '\\' + str(name) + '\\niijpg')
        maxx = 0
        maxname = 'x'
        for name2 in names2:
            img = cv2.imread(di + '\\' + str(name) + '\\niijpg' + '\\' + str(name2))
            t = img.sum()
            if(t>maxx):
                maxx = t
                maxname = name2
        print(maxname,":",maxx)
        
        img = cv2.imread(di + '\\' + str(name) + '\\niijpg' + '\\' + str(maxname))
        img = img[:,:,1]
        x=[]
        y=[]
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if(img[i][j]!=0):
                    x.append(j)
                    y.append(i)
        left = min(x)
        right = max(x)
        up = min(y)
        down = max(y)
        print(left,right,up,down)
        l = right - left
        w = down - up
        length = max(length,l)
        width = max(width,w)
        picname.append(maxname)
        midname.append(name)
        mid.append([round((left+right)/2,0),round((up+down)/2,0)])
        
    return midname,picname,mid,length,width

def Cut(midname,picname,mid,length,width,di,outpath):
    for k in range(len(midname)):
        img = cv2.imread(di + '\\' + str(midname[k]) + '\\jpg' + '\\' + str(picname[k]))
        midx = mid[k][0]
        midy = mid[k][1]
        left = int(midx) - int(length/2)
        right = int(midx) + int(length/2)
        up = int(midy) - int(width/2)
        down = int(midy) + int(width/2)
        img2 =  img[int(up):int(down),int(left):int(right)]
        out_path = outpath + '\\' + str(midname[k]) + '.jpg'
        cv2.imwrite(out_path,img2)

def GscaleNiijpg(file_path,ADV):
    n1 = nib.load(file_path + '\\' + ADV + '.nii.gz')
    n1 = n1.get_fdata()

    print(n1.shape)
    if(os.path.exists(file_path + '\\jpg')):
        shutil.rmtree(file_path + '\\jpg')
    if(not os.path.exists(file_path + '\\jpg')):
        os.mkdir(file_path + '\\jpg')
    for i in range(n1.shape[2]):
        out_path = file_path +"\\jpg\\" + str(i) + ".jpg"
        n1[:,:,i]=np.rot90(n1[:,:,i])
        n1[:,:,i]=np.rot90(n1[:,:,i])
        n1[:,:,i]=np.rot90(n1[:,:,i])
        n1[:,:,i]=cv2.flip(n1[:,:,i],1)
        imageio.imwrite(out_path,n1[:,:,i])
  
def OriNiijpg(file_path):
    n1 = nib.load(file_path + '\\' + 'Ori.nii.gz')
    n1 = n1.get_fdata()

    print(n1.shape)
    if(os.path.exists(file_path + '\\orijpg')):
        shutil.rmtree(file_path + '\\orijpg')
    if(not os.path.exists(file_path + '\\orijpg')):
        os.mkdir(file_path + '\\orijpg')
    for i in range(n1.shape[2]):
        out_path = file_path +"\\orijpg\\" + str(i) + ".jpg"
        n1[:,:,i]=np.rot90(n1[:,:,i])
        n1[:,:,i]=np.rot90(n1[:,:,i])
        n1[:,:,i]=np.rot90(n1[:,:,i])
        n1[:,:,i]=cv2.flip(n1[:,:,i],1)
        imageio.imwrite(out_path,n1[:,:,i])
        
def Niijpg(file_path,ADV):
    n1 = nib.load(file_path + '\\' + ADV + '.nii')
    n1 = n1.get_data()
    n1 = n1*255

    if(os.path.exists(file_path + '\\niijpg')):
        shutil.rmtree(file_path + '\\niijpg')
    if(not os.path.exists(file_path + '\\niijpg')):
        os.mkdir(file_path + '\\niijpg')
    for i in range(n1.shape[2]):
        out_path = file_path +"\\niijpg\\" + str(i) + ".jpg"
        n1[:,:,i]=np.rot90(n1[:,:,i])
        n1[:,:,i]=np.rot90(n1[:,:,i])
        n1[:,:,i]=np.rot90(n1[:,:,i])
        n1[:,:,i]=cv2.flip(n1[:,:,i],1)
        cv2.imwrite(out_path,n1[:,:,i])

di = r'WAIFUFA'
A = di + '\\' + 'A'
D = di + '\\' + 'D'
V = di + '\\' + 'V'

###############################################################################  
names = os.listdir(A)
for c in names:
    print(c)
    GscaleNiijpg(A + '\\' + str(c),str(c))
for c in names:
    print(c)
    GscaleNiijpg(D + '\\' + str(c),str(c))
for c in names:
    print(c)
    GscaleNiijpg(V + '\\' + str(c),str(c))

for c in names:
    print(c)
    OriNiijpg(A + '\\' + str(c))
for c in names:
    print(c)
    OriNiijpg(D + '\\' + str(c))
for c in names:
    print(c)
    OriNiijpg(V + '\\' + str(c))
############################################################################## 
names = os.listdir(A)
for c in names:
    print(c)
    Niijpg(A + '\\' + str(c),'A')
    
names = os.listdir(D)
for c in names:
    print(c)
    Niijpg(D + '\\' + str(c),'D')
    
names = os.listdir(V)
for c in names:
    print(c)
    Niijpg(V + '\\' + str(c),'V')
############################################################################### 
############################################################################### 

di = r'WAIWEIFUFA'
A = di + '\\' + 'A'
D = di + '\\' + 'D'
V = di + '\\' + 'V'

###############################################################################  
names = os.listdir(A)
for c in names:
    print(c)
    GscaleNiijpg(A + '\\' + str(c),str(c))
for c in names:
    print(c)
    GscaleNiijpg(D + '\\' + str(c),str(c))
for c in names:
    print(c)
    GscaleNiijpg(V + '\\' + str(c),str(c))

for c in names:
    print(c)
    OriNiijpg(A + '\\' + str(c))
for c in names:
    print(c)
    OriNiijpg(D + '\\' + str(c))
for c in names:
    print(c)
    OriNiijpg(V + '\\' + str(c))
############################################################################## 
names = os.listdir(A)
for c in names:
    print(c)
    Niijpg(A + '\\' + str(c),'A')
    
names = os.listdir(D)
for c in names:
    print(c)
    Niijpg(D + '\\' + str(c),'D')
    
names = os.listdir(V)
for c in names:
    print(c)
    Niijpg(V + '\\' + str(c),'V')
############################################################################### 

