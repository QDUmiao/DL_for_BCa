import numpy as np
import os
import cv2

def gama_transfer(img,power1):
    if len(img.shape) == 3:
         img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = 255*np.power(img/255,power1)
    img = np.around(img)
    img[img>255] = 255
    out_img = img.astype(np.uint8)
    return out_img

BF = r'C:\Users\Miao\Desktop\BF'
BW = r'C:\Users\Miao\Desktop\BW'
WF = r'C:\Users\Miao\Desktop\WF'
WW = r'C:\Users\Miao\Desktop\WW'

BFA = BF + '\\' + 'A'
BFD = BF + '\\' + 'D'
BFV = BF + '\\' + 'V'
BWA = BW + '\\' + 'A'
BWD = BW + '\\' + 'D'
BWV = BW + '\\' + 'V'
WFA = WF + '\\' + 'A'
WFD = WF + '\\' + 'D'
WFV = WF + '\\' + 'V'
WWA = WW + '\\' + 'A'
WWD = WW + '\\' + 'D'
WWV = WW + '\\' + 'V'
BFADV = BF + '\\' + 'ADV'
BWADV = BW + '\\' + 'ADV'
WFADV = WF + '\\' + 'ADV'
WWADV = WW + '\\' + 'ADV'
BFT = BF + '\\' + 'T'
BWT = BW + '\\' + 'T'
WFT = WF + '\\' + 'T'
WWT = WW + '\\' + 'T'
BFTA = BF + '\\' + 'TA'
BWTA = BW + '\\' + 'TA'
WFTA = WF + '\\' + 'TA'
WWTA = WW + '\\' + 'TA'
BFTD = BF + '\\' + 'TD'
BWTD = BW + '\\' + 'TD'
WFTD = WF + '\\' + 'TD'
WWTD = WW + '\\' + 'TD'
BFTV = BF + '\\' + 'TV'
BWTV = BW + '\\' + 'TV'
WFTV = WF + '\\' + 'TV'
WWTV = WW + '\\' + 'TV'

if(not os.path.exists(BFT)):
    os.mkdir(BFT)
    os.mkdir(BFTA)
    os.mkdir(BFTD)
    os.mkdir(BFTV)
    os.mkdir(BFADV)
if(not os.path.exists(BWT)):
    os.mkdir(BWT)
    os.mkdir(BWTA)
    os.mkdir(BWTD)
    os.mkdir(BWTV)
    os.mkdir(BWADV)
if(not os.path.exists(WFT)):
    os.mkdir(WFT)
    os.mkdir(WFTA)
    os.mkdir(WFTD)
    os.mkdir(WFTV)
    os.mkdir(WFADV)
if(not os.path.exists(WWT)):
    os.mkdir(WWT)
    os.mkdir(WWTA)
    os.mkdir(WWTD)
    os.mkdir(WWTV)
    os.mkdir(WWADV)
    
names = os.listdir(BFA)
for name in names:
    iA = BFA + '\\' + name
    iD = BFD + '\\' + name
    iV = BFV + '\\' + name

    imgA = cv2.imread(iA)
    imgD = cv2.imread(iD)
    imgV = cv2.imread(iV)
    
    imgA = cv2.cvtColor(imgA,cv2.COLOR_BGR2GRAY)
    imgD = cv2.cvtColor(imgD,cv2.COLOR_BGR2GRAY)
    imgV = cv2.cvtColor(imgV,cv2.COLOR_BGR2GRAY)

    imgADV = cv2.merge([imgA, imgD, imgV])
    OUTADV = BFADV + '\\' + name
    cv2.imwrite(OUTADV,imgADV)

    imgA = (imgA  - np.min(imgA)) / (np.max(imgA) - np.min(imgA))
    imgA = imgA*255
    
    imgD = (imgD  - np.min(imgD)) / (np.max(imgD) - np.min(imgD))
    imgD = imgD*255
    
    imgV = (imgV - np.min(imgV)) / (np.max(imgV) - np.min(imgV))
    imgV = imgV*255
    
    res = cv2.merge([imgA, imgD, imgV])
    OUT = BFT + '\\' + name
    OUTA = BFTA + '\\' + name
    OUTD = BFTD + '\\' + name
    OUTV = BFTV + '\\' + name
    cv2.imwrite(OUT,res)#T
    cv2.imwrite(OUTA,imgA)#TA
    cv2.imwrite(OUTD,imgD)#TD
    cv2.imwrite(OUTV,imgV)#TV
    
    img90A = cv2.rotate(imgA, cv2.ROTATE_90_CLOCKWISE)
    img90D = cv2.rotate(imgD, cv2.ROTATE_90_CLOCKWISE)
    img90V = cv2.rotate(imgV, cv2.ROTATE_90_CLOCKWISE)
    img180A = cv2.rotate(imgA, cv2.ROTATE_180)
    img180D = cv2.rotate(imgD, cv2.ROTATE_180)
    img180V = cv2.rotate(imgV, cv2.ROTATE_180)
    img270A = cv2.rotate(imgA, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270D = cv2.rotate(imgD, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270V = cv2.rotate(imgV, cv2.ROTATE_90_COUNTERCLOCKWISE)
    res90 = cv2.merge([img90A, img90D, img90V])
    res180 = cv2.merge([img180A, img180D, img180V])
    res270 = cv2.merge([img270A, img270D, img270V])
    OUT90 = BFT + '\\R90' + name
    OUT180 = BFT + '\\R180' + name
    OUT270 = BFT + '\\R270' + name
    OUT90A = BFTA + '\\R90' + name
    OUT90D = BFTD + '\\R90' + name
    OUT90V = BFTV + '\\R90' + name
    OUT180A = BFTA + '\\R180' + name
    OUT180D = BFTD + '\\R180' + name
    OUT180V = BFTV + '\\R180' + name
    OUT270A = BFTA + '\\R270' + name
    OUT270D = BFTD + '\\R270' + name
    OUT270V = BFTV + '\\R270' + name
    cv2.imwrite(OUT90,res90)
    cv2.imwrite(OUT90A,img90A)
    cv2.imwrite(OUT90D,img90D)
    cv2.imwrite(OUT90V,img90V)
    cv2.imwrite(OUT180,res180)
    cv2.imwrite(OUT180A,img180A)
    cv2.imwrite(OUT180D,img180D)
    cv2.imwrite(OUT180V,img180V)
    cv2.imwrite(OUT270,res270)
    cv2.imwrite(OUT270A,img270A)
    cv2.imwrite(OUT270D,img270D)
    cv2.imwrite(OUT270V,img270V)


    

    
names = os.listdir(BWA)
for name in names:
    iA = BWA + '\\' + name
    iD = BWD + '\\' + name
    iV = BWV + '\\' + name
    
    imgA = cv2.imread(iA)
    imgD = cv2.imread(iD)
    imgV = cv2.imread(iV)
    
    imgA = cv2.cvtColor(imgA,cv2.COLOR_BGR2GRAY)
    imgD = cv2.cvtColor(imgD,cv2.COLOR_BGR2GRAY)
    imgV = cv2.cvtColor(imgV,cv2.COLOR_BGR2GRAY)
    
    imgADV = cv2.merge([imgA, imgD, imgV])
    OUTADV = BWADV + '\\' + name
    cv2.imwrite(OUTADV,imgADV)

    imgA = (imgA  - np.min(imgA)) / (np.max(imgA) - np.min(imgA))
    imgA = imgA*255
    
    imgD = (imgD  - np.min(imgD)) / (np.max(imgD) - np.min(imgD))
    imgD = imgD*255
    
    imgV = (imgV - np.min(imgV)) / (np.max(imgV) - np.min(imgV))
    imgV = imgV*255

    res = cv2.merge([imgA, imgD, imgV])
    OUT = BWT + '\\' + name
    OUTA = BWTA + '\\' + name
    OUTD = BWTD + '\\' + name
    OUTV = BWTV + '\\' + name
    cv2.imwrite(OUT,res)
    cv2.imwrite(OUTA,imgA)
    cv2.imwrite(OUTD,imgD)
    cv2.imwrite(OUTV,imgV)
    
    img90A = cv2.rotate(imgA, cv2.ROTATE_90_CLOCKWISE)
    img90D = cv2.rotate(imgD, cv2.ROTATE_90_CLOCKWISE)
    img90V = cv2.rotate(imgV, cv2.ROTATE_90_CLOCKWISE)
    img180A = cv2.rotate(imgA, cv2.ROTATE_180)
    img180D = cv2.rotate(imgD, cv2.ROTATE_180)
    img180V = cv2.rotate(imgV, cv2.ROTATE_180)
    img270A = cv2.rotate(imgA, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270D = cv2.rotate(imgD, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270V = cv2.rotate(imgV, cv2.ROTATE_90_COUNTERCLOCKWISE)
    res90 = cv2.merge([img90A, img90D, img90V])
    res180 = cv2.merge([img180A, img180D, img180V])
    res270 = cv2.merge([img270A, img270D, img270V])
    OUT90 = BWT + '\\R90' + name
    OUT180 = BWT + '\\R180' + name
    OUT270 = BWT + '\\R270' + name
    OUT90A = BWTA + '\\R90' + name
    OUT90D = BWTD + '\\R90' + name
    OUT90V = BWTV + '\\R90' + name
    OUT180A = BWTA + '\\R180' + name
    OUT180D = BWTD + '\\R180' + name
    OUT180V = BWTV + '\\R180' + name
    OUT270A = BWTA + '\\R270' + name
    OUT270D = BWTD + '\\R270' + name
    OUT270V = BWTV + '\\R270' + name
    cv2.imwrite(OUT90,res90)
    cv2.imwrite(OUT90A,img90A)
    cv2.imwrite(OUT90D,img90D)
    cv2.imwrite(OUT90V,img90V)
    cv2.imwrite(OUT180,res180)
    cv2.imwrite(OUT180A,img180A)
    cv2.imwrite(OUT180D,img180D)
    cv2.imwrite(OUT180V,img180V)
    cv2.imwrite(OUT270,res270)
    cv2.imwrite(OUT270A,img270A)
    cv2.imwrite(OUT270D,img270D)
    cv2.imwrite(OUT270V,img270V)
    
    

    
    
names = os.listdir(WFA)
for name in names:
    iA = WFA + '\\' + name
    iD = WFD + '\\' + name
    iV = WFV + '\\' + name
    
    imgA = cv2.imread(iA)
    imgD = cv2.imread(iD)
    imgV = cv2.imread(iV)
    
    imgA = cv2.cvtColor(imgA,cv2.COLOR_BGR2GRAY)
    imgD = cv2.cvtColor(imgD,cv2.COLOR_BGR2GRAY)
    imgV = cv2.cvtColor(imgV,cv2.COLOR_BGR2GRAY)
    
    imgADV = cv2.merge([imgA, imgD, imgV])
    OUTADV = WFADV + '\\' + name
    cv2.imwrite(OUTADV,imgADV)
    imgA = (imgA  - np.min(imgA)) / (np.max(imgA) - np.min(imgA))
    imgA = imgA*255
    
    imgD = (imgD  - np.min(imgD)) / (np.max(imgD) - np.min(imgD))
    imgD = imgD*255
    
    imgV = (imgV - np.min(imgV)) / (np.max(imgV) - np.min(imgV))
    imgV = imgV*255

    res = cv2.merge([imgA, imgD, imgV])
    OUT = WFT + '\\' + name
    OUTA = WFTA + '\\' + name
    OUTD = WFTD + '\\' + name
    OUTV = WFTV + '\\' + name
    cv2.imwrite(OUT,res)
    cv2.imwrite(OUTA,imgA)
    cv2.imwrite(OUTD,imgD)
    cv2.imwrite(OUTV,imgV)
    

    
    
names = os.listdir(WWA)
for name in names:
    iA = WWA + '\\' + name
    iD = WWD + '\\' + name
    iV = WWV + '\\' + name
    
    imgA = cv2.imread(iA)
    imgD = cv2.imread(iD)
    imgV = cv2.imread(iV)
    
    imgA = cv2.cvtColor(imgA,cv2.COLOR_BGR2GRAY)
    imgD = cv2.cvtColor(imgD,cv2.COLOR_BGR2GRAY)
    imgV = cv2.cvtColor(imgV,cv2.COLOR_BGR2GRAY)
    
    imgADV = cv2.merge([imgA, imgD, imgV])
    OUTADV = WWADV + '\\' + name
    cv2.imwrite(OUTADV,imgADV)

    imgA = (imgA  - np.min(imgA)) / (np.max(imgA) - np.min(imgA))
    imgA = imgA*255
    
    imgD = (imgD  - np.min(imgD)) / (np.max(imgD) - np.min(imgD))
    imgD = imgD*255
    
    imgV = (imgV - np.min(imgV)) / (np.max(imgV) - np.min(imgV))
    imgV = imgV*255

    res = cv2.merge([imgA, imgD, imgV])
    OUT = WWT + '\\' + name
    OUTA = WWTA + '\\' + name
    OUTD = WWTD + '\\' + name
    OUTV = WWTV + '\\' + name
    cv2.imwrite(OUT,res)
    cv2.imwrite(OUTA,imgA)
    cv2.imwrite(OUTD,imgD)
    cv2.imwrite(OUTV,imgV)
    

    
