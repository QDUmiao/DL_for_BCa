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
    cv2.imwrite(OUT,res)
    cv2.imwrite(OUTA,imgA)
    cv2.imwrite(OUTD,imgD)
    cv2.imwrite(OUTV,imgV)
   
    ##gamma0.5
    gamma09A =  gama_transfer(imgA,0.9)
    gamma09D =  gama_transfer(imgD,0.9)
    gamma09V =  gama_transfer(imgV,0.9)
    res = cv2.merge([gamma09A, gamma09D, gamma09V])
    OUT = BFT + '\\GM09' + name
    OUTA = BFTA + '\\GM09' + name
    OUTD = BFTD + '\\GM09' + name
    OUTV = BFTV + '\\GM09' + name
    cv2.imwrite(OUT,res)
    cv2.imwrite(OUTA,gamma09A)
    cv2.imwrite(OUTD,gamma09D)
    cv2.imwrite(OUTV,gamma09V)

    ##gamma1.5
    gamma11A =  gama_transfer(imgA,1.1)
    gamma11D =  gama_transfer(imgD,1.1)
    gamma11V =  gama_transfer(imgV,1.1)
    res = cv2.merge([gamma11A, gamma11D, gamma11V])
    OUT = BFT + '\\GM11' + name
    OUTA = BFTA + '\\GM11' + name
    OUTD = BFTD + '\\GM11' + name
    OUTV = BFTV + '\\GM11' + name
    cv2.imwrite(OUT,res)
    cv2.imwrite(OUTA,gamma11A)
    cv2.imwrite(OUTD,gamma11D)
    cv2.imwrite(OUTV,gamma11V)
    
    ##GAUSS
    noiseA = np.random.normal(0,1, np.array(imgA).shape)
    noiseD = np.random.normal(0,1, np.array(imgD).shape)
    noiseV = np.random.normal(0,1, np.array(imgV).shape)
    gaussA = imgA + noiseA
    gaussD = imgD + noiseD
    gaussV = imgV + noiseV
    res = cv2.merge([gaussA, gaussD, gaussV])
    OUT = BFT + '\\GAUSS' + name
    OUTA = BFTA + '\\GAUSS' + name
    OUTD = BFTD + '\\GAUSS' + name
    OUTV = BFTV + '\\GAUSS' + name
    cv2.imwrite(OUT,res)
    cv2.imwrite(OUTA,gamma11A)
    cv2.imwrite(OUTD,gamma11D)
    cv2.imwrite(OUTV,gamma11V)
    
    ##gamma0.5+GAUSS
    noiseA = np.random.normal(0,1, np.array(gamma09A).shape)
    noiseD = np.random.normal(0,1, np.array(gamma09D).shape)
    noiseV = np.random.normal(0,1, np.array(gamma09V).shape)
    GM09gaussA = gamma09A + noiseA
    GM09gaussD = gamma09D + noiseD
    GM09gaussV = gamma09V + noiseV
    res = cv2.merge([GM09gaussA, GM09gaussD, GM09gaussV])
    OUT = BFT + '\\GM09GAUSS' + name
    OUTA = BFTA + '\\GM09GAUSS' + name
    OUTD = BFTD + '\\GM09GAUSS' + name
    OUTV = BFTV + '\\GM09GAUSS' + name
    cv2.imwrite(OUT,res)
    cv2.imwrite(OUTA,GM09gaussA)
    cv2.imwrite(OUTD,GM09gaussD)
    cv2.imwrite(OUTV,GM09gaussV)
    
    ##gamma1.5+GAUSS
    noiseA = np.random.normal(0,1, np.array(gamma11A).shape)
    noiseD = np.random.normal(0,1, np.array(gamma11D).shape)
    noiseV = np.random.normal(0,1, np.array(gamma11V).shape)
    GM11gaussA = gamma11A + noiseA
    GM11gaussD = gamma11D + noiseD
    GM11gaussV = gamma11V + noiseV
    res = cv2.merge([GM11gaussA, GM11gaussD, GM11gaussV])
    OUT = BFT + '\\GM11GAUSS' + name
    OUTA = BFTA + '\\GM11GAUSS' + name
    OUTD = BFTD + '\\GM11GAUSS' + name
    OUTV = BFTV + '\\GM11GAUSS' + name
    cv2.imwrite(OUT,res)
    cv2.imwrite(OUTA,GM11gaussA)
    cv2.imwrite(OUTD,GM11gaussD)
    cv2.imwrite(OUTV,GM11gaussV)
    
    ##旋转90 180 270
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
    
    
    ##gamma0.5旋转90 180 270
    img90A = cv2.rotate(gamma09A, cv2.ROTATE_90_CLOCKWISE)
    img90D = cv2.rotate(gamma09D, cv2.ROTATE_90_CLOCKWISE)
    img90V = cv2.rotate(gamma09V, cv2.ROTATE_90_CLOCKWISE)
    img180A = cv2.rotate(gamma09A, cv2.ROTATE_180)
    img180D = cv2.rotate(gamma09D, cv2.ROTATE_180)
    img180V = cv2.rotate(gamma09V, cv2.ROTATE_180)
    img270A = cv2.rotate(gamma09A, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270D = cv2.rotate(gamma09D, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270V = cv2.rotate(gamma09V, cv2.ROTATE_90_COUNTERCLOCKWISE)
    res90 = cv2.merge([img90A, img90D, img90V])
    res180 = cv2.merge([img180A, img180D, img180V])
    res270 = cv2.merge([img270A, img270D, img270V])
    OUT90 = BFT + '\\GM09R90' + name
    OUT180 = BFT + '\\GM09R180' + name
    OUT270 = BFT + '\\GM09R270' + name
    OUT90A = BFTA + '\\GM09R90' + name
    OUT90D = BFTD + '\\GM09R90' + name
    OUT90V = BFTV + '\\GM09R90' + name
    OUT180A = BFTA + '\\GM09R180' + name
    OUT180D = BFTD + '\\GM09R180' + name
    OUT180V = BFTV + '\\GM09R180' + name
    OUT270A = BFTA + '\\GM09R270' + name
    OUT270D = BFTD + '\\GM09R270' + name
    OUT270V = BFTV + '\\GM09R270' + name
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
    ##gamma1.5旋转90 180 270
    img90A = cv2.rotate(gamma11A, cv2.ROTATE_90_CLOCKWISE)
    img90D = cv2.rotate(gamma11D, cv2.ROTATE_90_CLOCKWISE)
    img90V = cv2.rotate(gamma11V, cv2.ROTATE_90_CLOCKWISE)
    img180A = cv2.rotate(gamma11A, cv2.ROTATE_180)
    img180D = cv2.rotate(gamma11D, cv2.ROTATE_180)
    img180V = cv2.rotate(gamma11V, cv2.ROTATE_180)
    img270A = cv2.rotate(gamma11A, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270D = cv2.rotate(gamma11D, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270V = cv2.rotate(gamma11V, cv2.ROTATE_90_COUNTERCLOCKWISE)
    res90 = cv2.merge([img90A, img90D, img90V])
    res180 = cv2.merge([img180A, img180D, img180V])
    res270 = cv2.merge([img270A, img270D, img270V])
    OUT90 = BFT + '\\GM11R90' + name
    OUT180 = BFT + '\\GM11R180' + name
    OUT270 = BFT + '\\GM11R270' + name
    OUT90A = BFTA + '\\GM11R90' + name
    OUT90D = BFTD + '\\GM11R90' + name
    OUT90V = BFTV + '\\GM11R90' + name
    OUT180A = BFTA + '\\GM11R180' + name
    OUT180D = BFTD + '\\GM11R180' + name
    OUT180V = BFTV + '\\GM11R180' + name
    OUT270A = BFTA + '\\GM11R270' + name
    OUT270D = BFTD + '\\GM11R270' + name
    OUT270V = BFTV + '\\GM11R270' + name
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
    ##GAUSS旋转90 180 270
    img90A = cv2.rotate(gaussA, cv2.ROTATE_90_CLOCKWISE)
    img90D = cv2.rotate(gaussD, cv2.ROTATE_90_CLOCKWISE)
    img90V = cv2.rotate(gaussV, cv2.ROTATE_90_CLOCKWISE)
    img180A = cv2.rotate(gaussA, cv2.ROTATE_180)
    img180D = cv2.rotate(gaussD, cv2.ROTATE_180)
    img180V = cv2.rotate(gaussV, cv2.ROTATE_180)
    img270A = cv2.rotate(gaussA, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270D = cv2.rotate(gaussD, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270V = cv2.rotate(gaussV, cv2.ROTATE_90_COUNTERCLOCKWISE)
    res90 = cv2.merge([img90A, img90D, img90V])
    res180 = cv2.merge([img180A, img180D, img180V])
    res270 = cv2.merge([img270A, img270D, img270V])
    OUT90 = BFT + '\\gaussR90' + name
    OUT180 = BFT + '\\gaussR180' + name
    OUT270 = BFT + '\\gaussR270' + name
    OUT90A = BFTA + '\\gaussR90' + name
    OUT90D = BFTD + '\\gaussR90' + name
    OUT90V = BFTV + '\\gaussR90' + name
    OUT180A = BFTA + '\\gaussR180' + name
    OUT180D = BFTD + '\\gaussR180' + name
    OUT180V = BFTV + '\\gaussR180' + name
    OUT270A = BFTA + '\\gaussR270' + name
    OUT270D = BFTD + '\\gaussR270' + name
    OUT270V = BFTV + '\\gaussR270' + name
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
    ##gamma0.5+GAUSS旋转90 180 270
    img90A = cv2.rotate(GM09gaussA, cv2.ROTATE_90_CLOCKWISE)
    img90D = cv2.rotate(GM09gaussD, cv2.ROTATE_90_CLOCKWISE)
    img90V = cv2.rotate(GM09gaussV, cv2.ROTATE_90_CLOCKWISE)
    img180A = cv2.rotate(GM09gaussA, cv2.ROTATE_180)
    img180D = cv2.rotate(GM09gaussD, cv2.ROTATE_180)
    img180V = cv2.rotate(GM09gaussV, cv2.ROTATE_180)
    img270A = cv2.rotate(GM09gaussA, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270D = cv2.rotate(GM09gaussD, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270V = cv2.rotate(GM09gaussV, cv2.ROTATE_90_COUNTERCLOCKWISE)
    res90 = cv2.merge([img90A, img90D, img90V])
    res180 = cv2.merge([img180A, img180D, img180V])
    res270 = cv2.merge([img270A, img270D, img270V])
    OUT90 = BFT + '\\GM09gaussR90' + name
    OUT180 = BFT + '\\GM09gaussR180' + name
    OUT270 = BFT + '\\GM09gaussR270' + name
    OUT90A = BFTA + '\\GM09gaussR90' + name
    OUT90D = BFTD + '\\GM09gaussR90' + name
    OUT90V = BFTV + '\\GM09gaussR90' + name
    OUT180A = BFTA + '\\GM09gaussR180' + name
    OUT180D = BFTD + '\\GM09gaussR180' + name
    OUT180V = BFTV + '\\GM09gaussR180' + name
    OUT270A = BFTA + '\\GM09gaussR270' + name
    OUT270D = BFTD + '\\GM09gaussR270' + name
    OUT270V = BFTV + '\\GM09gaussR270' + name
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
    ##gamma1.5+GAUSS旋转90 180 270
    img90A = cv2.rotate(GM11gaussA, cv2.ROTATE_90_CLOCKWISE)
    img90D = cv2.rotate(GM11gaussD, cv2.ROTATE_90_CLOCKWISE)
    img90V = cv2.rotate(GM11gaussV, cv2.ROTATE_90_CLOCKWISE)
    img180A = cv2.rotate(GM11gaussA, cv2.ROTATE_180)
    img180D = cv2.rotate(GM11gaussD, cv2.ROTATE_180)
    img180V = cv2.rotate(GM11gaussV, cv2.ROTATE_180)
    img270A = cv2.rotate(GM11gaussA, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270D = cv2.rotate(GM11gaussD, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img270V = cv2.rotate(GM11gaussV, cv2.ROTATE_90_COUNTERCLOCKWISE)
    res90 = cv2.merge([img90A, img90D, img90V])
    res180 = cv2.merge([img180A, img180D, img180V])
    res270 = cv2.merge([img270A, img270D, img270V])
    OUT90 = BFT + '\\GM11gaussR90' + name
    OUT180 = BFT + '\\GM11gaussR180' + name
    OUT270 = BFT + '\\GM11gaussR270' + name
    OUT90A = BFTA + '\\GM11gaussR90' + name
    OUT90D = BFTD + '\\GM11gaussR90' + name
    OUT90V = BFTV + '\\GM11gaussR90' + name
    OUT180A = BFTA + '\\GM11gaussR180' + name
    OUT180D = BFTD + '\\GM11gaussR180' + name
    OUT180V = BFTV + '\\GM11gaussR180' + name
    OUT270A = BFTA + '\\GM11gaussR270' + name
    OUT270D = BFTD + '\\GM11gaussR270' + name
    OUT270V = BFTV + '\\GM11gaussR270' + name
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
