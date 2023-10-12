import numpy as np
import os
import cv2
from PIL import Image

def gama_transfer(img,power1):
    if len(img.shape) == 3:
         img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = 255*np.power(img/255,power1)
    img = np.around(img)
    img[img>255] = 255
    out_img = img.astype(np.uint8)
    return out_img

BF = r'BF0'
BW = r'BW0'
WF = r'WF0'
WW = r'WW0'

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
    
    imgA = Image.fromarray(np.uint8(imgA))
    imgD = Image.fromarray(np.uint8(imgD))
    imgV = Image.fromarray(np.uint8(imgV))
    
    img30A = imgA.rotate(360-30,expand=True)
    img30D = imgD.rotate(360-30,expand=True)
    img30V = imgV.rotate(360-30,expand=True)
    img60A = imgA.rotate(360-60,expand=True)
    img60D = imgD.rotate(360-60,expand=True)
    img60V = imgV.rotate(360-60,expand=True)
    img90A = imgA.rotate(360-90,expand=True)
    img90D = imgD.rotate(360-90,expand=True)
    img90V = imgV.rotate(360-90,expand=True)
    img120A = imgA.rotate(360-120,expand=True)
    img120D = imgD.rotate(360-120,expand=True)
    img120V = imgV.rotate(360-120,expand=True)
    img150A = imgA.rotate(360-150,expand=True)
    img150D = imgD.rotate(360-150,expand=True)
    img150V = imgV.rotate(360-150,expand=True)
    img180A = imgA.rotate(360-180,expand=True)
    img180D = imgD.rotate(360-180,expand=True)
    img180V = imgV.rotate(360-180,expand=True)
    img210A = imgA.rotate(360-210,expand=True)
    img210D = imgD.rotate(360-210,expand=True)
    img210V = imgV.rotate(360-210,expand=True)
    img240A = imgA.rotate(360-240,expand=True)
    img240D = imgD.rotate(360-240,expand=True)
    img240V = imgV.rotate(360-240,expand=True)
    img270A = imgA.rotate(360-270,expand=True)
    img270D = imgD.rotate(360-270,expand=True)
    img270V = imgV.rotate(360-270,expand=True)
    img300A = imgA.rotate(360-300,expand=True)
    img300D = imgD.rotate(360-300,expand=True)
    img300V = imgV.rotate(360-300,expand=True)
    img330A = imgA.rotate(360-330,expand=True)
    img330D = imgD.rotate(360-330,expand=True)
    img330V = imgV.rotate(360-330,expand=True)
    img30A = np.array(img30A)
    img30D = np.array(img30D)
    img30V = np.array(img30V)
    img60A = np.array(img60A)
    img60D = np.array(img60D)
    img60V = np.array(img60V)
    img90A = np.array(img90A)
    img90D = np.array(img90D)
    img90V = np.array(img90V)
    img120A = np.array(img120A)
    img120D = np.array(img120D)
    img120V = np.array(img120V)
    img150A = np.array(img150A)
    img150D = np.array(img150D)
    img150V = np.array(img150V)
    img180A = np.array(img180A)
    img180D = np.array(img180D)
    img180V = np.array(img180V)
    img210A = np.array(img210A)
    img210D = np.array(img210D)
    img210V = np.array(img210V)
    img240A = np.array(img240A)
    img240D = np.array(img240D)
    img240V = np.array(img240V)
    img270A = np.array(img270A)
    img270D = np.array(img270D)
    img270V = np.array(img270V)
    img300A = np.array(img300A)
    img300D = np.array(img300D)
    img300V = np.array(img300V)
    img330A = np.array(img330A)
    img330D = np.array(img330D)
    img330V = np.array(img330V)
    
    res30 = cv2.merge([img30A, img30D, img30V])
    res60 = cv2.merge([img60A, img60D, img60V])
    res90 = cv2.merge([img90A, img90D, img90V])
    res120 = cv2.merge([img120A, img120D, img120V])
    res150 = cv2.merge([img150A, img150D, img150V])
    res180 = cv2.merge([img180A, img180D, img180V])
    res210 = cv2.merge([img210A, img210D, img210V])
    res240 = cv2.merge([img240A, img240D, img240V])
    res270 = cv2.merge([img270A, img270D, img270V])
    res300 = cv2.merge([img300A, img300D, img300V])
    res330 = cv2.merge([img330A, img330D, img330V])
    
    OUT30 = BFT + '\\R30' + name
    OUT60 = BFT + '\\R60' + name
    OUT90 = BFT + '\\R90' + name
    OUT120 = BFT + '\\R120' + name
    OUT150 = BFT + '\\R150' + name
    OUT180 = BFT + '\\R180' + name
    OUT210 = BFT + '\\R210' + name
    OUT240 = BFT + '\\R240' + name
    OUT270 = BFT + '\\R270' + name
    OUT300 = BFT + '\\R300' + name
    OUT330 = BFT + '\\R330' + name
    
    OUT30A = BFTA + '\\R30' + name
    OUT30D = BFTD + '\\R30' + name
    OUT30V = BFTV + '\\R30' + name
    OUT60A = BFTA + '\\R60' + name
    OUT60D = BFTD + '\\R60' + name
    OUT60V = BFTV + '\\R60' + name
    OUT90A = BFTA + '\\R90' + name
    OUT90D = BFTD + '\\R90' + name
    OUT90V = BFTV + '\\R90' + name
    OUT120A = BFTA + '\\R120' + name
    OUT120D = BFTD + '\\R120' + name
    OUT120V = BFTV + '\\R120' + name
    OUT150A = BFTA + '\\R150' + name
    OUT150D = BFTD + '\\R150' + name
    OUT150V = BFTV + '\\R150' + name
    OUT180A = BFTA + '\\R180' + name
    OUT180D = BFTD + '\\R180' + name
    OUT180V = BFTV + '\\R180' + name
    OUT210A = BFTA + '\\R210' + name
    OUT210D = BFTD + '\\R210' + name
    OUT210V = BFTV + '\\R210' + name
    OUT240A = BFTA + '\\R240' + name
    OUT240D = BFTD + '\\R240' + name
    OUT240V = BFTV + '\\R240' + name
    OUT270A = BFTA + '\\R270' + name
    OUT270D = BFTD + '\\R270' + name
    OUT270V = BFTV + '\\R270' + name
    OUT300A = BFTA + '\\R300' + name
    OUT300D = BFTD + '\\R300' + name
    OUT300V = BFTV + '\\R300' + name
    OUT330A = BFTA + '\\R330' + name
    OUT330D = BFTD + '\\R330' + name
    OUT330V = BFTV + '\\R330' + name
    cv2.imwrite(OUT30,res30)
    cv2.imwrite(OUT30A,img30A)
    cv2.imwrite(OUT30D,img30D)
    cv2.imwrite(OUT30V,img30V)
    cv2.imwrite(OUT60,res60)
    cv2.imwrite(OUT60A,img60A)
    cv2.imwrite(OUT60D,img60D)
    cv2.imwrite(OUT60V,img60V)
    cv2.imwrite(OUT90,res90)
    cv2.imwrite(OUT90A,img90A)
    cv2.imwrite(OUT90D,img90D)
    cv2.imwrite(OUT90V,img90V)
    cv2.imwrite(OUT120,res120)
    cv2.imwrite(OUT120A,img120A)
    cv2.imwrite(OUT120D,img120D)
    cv2.imwrite(OUT120V,img120V)
    cv2.imwrite(OUT150,res150)
    cv2.imwrite(OUT150A,img150A)
    cv2.imwrite(OUT150D,img150D)
    cv2.imwrite(OUT150V,img150V)
    cv2.imwrite(OUT180,res180)
    cv2.imwrite(OUT180A,img180A)
    cv2.imwrite(OUT180D,img180D)
    cv2.imwrite(OUT180V,img180V)
    cv2.imwrite(OUT210,res210)
    cv2.imwrite(OUT210A,img210A)
    cv2.imwrite(OUT210D,img210D)
    cv2.imwrite(OUT210V,img210V)
    cv2.imwrite(OUT240,res240)
    cv2.imwrite(OUT240A,img240A)
    cv2.imwrite(OUT240D,img240D)
    cv2.imwrite(OUT240V,img240V)
    cv2.imwrite(OUT270,res270)
    cv2.imwrite(OUT270A,img270A)
    cv2.imwrite(OUT270D,img270D)
    cv2.imwrite(OUT270V,img270V)
    cv2.imwrite(OUT300,res300)
    cv2.imwrite(OUT300A,img300A)
    cv2.imwrite(OUT300D,img300D)
    cv2.imwrite(OUT300V,img300V)
    cv2.imwrite(OUT330,res330)
    cv2.imwrite(OUT330A,img330A)
    cv2.imwrite(OUT330D,img330D)
    cv2.imwrite(OUT330V,img330V)
    

    

    
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
    

    
    imgA = Image.fromarray(np.uint8(imgA))
    imgD = Image.fromarray(np.uint8(imgD))
    imgV = Image.fromarray(np.uint8(imgV))
    
    img30A = imgA.rotate(360-30,expand=True)
    img30D = imgD.rotate(360-30,expand=True)
    img30V = imgV.rotate(360-30,expand=True)
    img60A = imgA.rotate(360-60,expand=True)
    img60D = imgD.rotate(360-60,expand=True)
    img60V = imgV.rotate(360-60,expand=True)
    img90A = imgA.rotate(360-90,expand=True)
    img90D = imgD.rotate(360-90,expand=True)
    img90V = imgV.rotate(360-90,expand=True)
    img120A = imgA.rotate(360-120,expand=True)
    img120D = imgD.rotate(360-120,expand=True)
    img120V = imgV.rotate(360-120,expand=True)
    img150A = imgA.rotate(360-150,expand=True)
    img150D = imgD.rotate(360-150,expand=True)
    img150V = imgV.rotate(360-150,expand=True)
    img180A = imgA.rotate(360-180,expand=True)
    img180D = imgD.rotate(360-180,expand=True)
    img180V = imgV.rotate(360-180,expand=True)
    img210A = imgA.rotate(360-210,expand=True)
    img210D = imgD.rotate(360-210,expand=True)
    img210V = imgV.rotate(360-210,expand=True)
    img240A = imgA.rotate(360-240,expand=True)
    img240D = imgD.rotate(360-240,expand=True)
    img240V = imgV.rotate(360-240,expand=True)
    img270A = imgA.rotate(360-270,expand=True)
    img270D = imgD.rotate(360-270,expand=True)
    img270V = imgV.rotate(360-270,expand=True)
    img300A = imgA.rotate(360-300,expand=True)
    img300D = imgD.rotate(360-300,expand=True)
    img300V = imgV.rotate(360-300,expand=True)
    img330A = imgA.rotate(360-330,expand=True)
    img330D = imgD.rotate(360-330,expand=True)
    img330V = imgV.rotate(360-330,expand=True)
    img30A = np.array(img30A)
    img30D = np.array(img30D)
    img30V = np.array(img30V)
    img60A = np.array(img60A)
    img60D = np.array(img60D)
    img60V = np.array(img60V)
    img90A = np.array(img90A)
    img90D = np.array(img90D)
    img90V = np.array(img90V)
    img120A = np.array(img120A)
    img120D = np.array(img120D)
    img120V = np.array(img120V)
    img150A = np.array(img150A)
    img150D = np.array(img150D)
    img150V = np.array(img150V)
    img180A = np.array(img180A)
    img180D = np.array(img180D)
    img180V = np.array(img180V)
    img210A = np.array(img210A)
    img210D = np.array(img210D)
    img210V = np.array(img210V)
    img240A = np.array(img240A)
    img240D = np.array(img240D)
    img240V = np.array(img240V)
    img270A = np.array(img270A)
    img270D = np.array(img270D)
    img270V = np.array(img270V)
    img300A = np.array(img300A)
    img300D = np.array(img300D)
    img300V = np.array(img300V)
    img330A = np.array(img330A)
    img330D = np.array(img330D)
    img330V = np.array(img330V)
    
    res30 = cv2.merge([img30A, img30D, img30V])
    res60 = cv2.merge([img60A, img60D, img60V])
    res90 = cv2.merge([img90A, img90D, img90V])
    res120 = cv2.merge([img120A, img120D, img120V])
    res150 = cv2.merge([img150A, img150D, img150V])
    res180 = cv2.merge([img180A, img180D, img180V])
    res210 = cv2.merge([img210A, img210D, img210V])
    res240 = cv2.merge([img240A, img240D, img240V])
    res270 = cv2.merge([img270A, img270D, img270V])
    res300 = cv2.merge([img300A, img300D, img300V])
    res330 = cv2.merge([img330A, img330D, img330V])
    
    OUT30 = BWT + '\\R30' + name
    OUT60 = BWT + '\\R60' + name
    OUT90 = BWT + '\\R90' + name
    OUT120 = BWT + '\\R120' + name
    OUT150 = BWT + '\\R150' + name
    OUT180 = BWT + '\\R180' + name
    OUT210 = BWT + '\\R210' + name
    OUT240 = BWT + '\\R240' + name
    OUT270 = BWT + '\\R270' + name
    OUT300 = BWT + '\\R300' + name
    OUT330 = BWT + '\\R330' + name
    
    OUT30A = BWTA + '\\R30' + name
    OUT30D = BWTD + '\\R30' + name
    OUT30V = BWTV + '\\R30' + name
    OUT60A = BWTA + '\\R60' + name
    OUT60D = BWTD + '\\R60' + name
    OUT60V = BWTV + '\\R60' + name
    OUT90A = BWTA + '\\R90' + name
    OUT90D = BWTD + '\\R90' + name
    OUT90V = BWTV + '\\R90' + name
    OUT120A = BWTA + '\\R120' + name
    OUT120D = BWTD + '\\R120' + name
    OUT120V = BWTV + '\\R120' + name
    OUT150A = BWTA + '\\R150' + name
    OUT150D = BWTD + '\\R150' + name
    OUT150V = BWTV + '\\R150' + name
    OUT180A = BWTA + '\\R180' + name
    OUT180D = BWTD + '\\R180' + name
    OUT180V = BWTV + '\\R180' + name
    OUT210A = BWTA + '\\R210' + name
    OUT210D = BWTD + '\\R210' + name
    OUT210V = BWTV + '\\R210' + name
    OUT240A = BWTA + '\\R240' + name
    OUT240D = BWTD + '\\R240' + name
    OUT240V = BWTV + '\\R240' + name
    OUT270A = BWTA + '\\R270' + name
    OUT270D = BWTD + '\\R270' + name
    OUT270V = BWTV + '\\R270' + name
    OUT300A = BWTA + '\\R300' + name
    OUT300D = BWTD + '\\R300' + name
    OUT300V = BWTV + '\\R300' + name
    OUT330A = BWTA + '\\R330' + name
    OUT330D = BWTD + '\\R330' + name
    OUT330V = BWTV + '\\R330' + name
    cv2.imwrite(OUT30,res30)
    cv2.imwrite(OUT30A,img30A)
    cv2.imwrite(OUT30D,img30D)
    cv2.imwrite(OUT30V,img30V)
    cv2.imwrite(OUT60,res60)
    cv2.imwrite(OUT60A,img60A)
    cv2.imwrite(OUT60D,img60D)
    cv2.imwrite(OUT60V,img60V)
    cv2.imwrite(OUT90,res90)
    cv2.imwrite(OUT90A,img90A)
    cv2.imwrite(OUT90D,img90D)
    cv2.imwrite(OUT90V,img90V)
    cv2.imwrite(OUT120,res120)
    cv2.imwrite(OUT120A,img120A)
    cv2.imwrite(OUT120D,img120D)
    cv2.imwrite(OUT120V,img120V)
    cv2.imwrite(OUT150,res150)
    cv2.imwrite(OUT150A,img150A)
    cv2.imwrite(OUT150D,img150D)
    cv2.imwrite(OUT150V,img150V)
    cv2.imwrite(OUT180,res180)
    cv2.imwrite(OUT180A,img180A)
    cv2.imwrite(OUT180D,img180D)
    cv2.imwrite(OUT180V,img180V)
    cv2.imwrite(OUT210,res210)
    cv2.imwrite(OUT210A,img210A)
    cv2.imwrite(OUT210D,img210D)
    cv2.imwrite(OUT210V,img210V)
    cv2.imwrite(OUT240,res240)
    cv2.imwrite(OUT240A,img240A)
    cv2.imwrite(OUT240D,img240D)
    cv2.imwrite(OUT240V,img240V)
    cv2.imwrite(OUT270,res270)
    cv2.imwrite(OUT270A,img270A)
    cv2.imwrite(OUT270D,img270D)
    cv2.imwrite(OUT270V,img270V)
    cv2.imwrite(OUT300,res300)
    cv2.imwrite(OUT300A,img300A)
    cv2.imwrite(OUT300D,img300D)
    cv2.imwrite(OUT300V,img300V)
    cv2.imwrite(OUT330,res330)
    cv2.imwrite(OUT330A,img330A)
    cv2.imwrite(OUT330D,img330D)
    cv2.imwrite(OUT330V,img330V)
    
    

    
    
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
    

    
