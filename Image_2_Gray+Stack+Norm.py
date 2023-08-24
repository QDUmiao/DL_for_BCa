import numpy as np
import os
import cv2

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

    imgADV = cv2.merge([imgV, imgD, imgV])
    OUTADV = BFADV + '\\' + name
    cv2.imwrite(OUTADV,imgADV)

    imgA = (imgA  - np.min(imgA)) / (np.max(imgA) - np.min(imgA))
    imgA = imgA*255
    
    imgD = (imgD  - np.min(imgD)) / (np.max(imgD) - np.min(imgD))
    imgD = imgD*255
    
    imgV = (imgV - np.min(imgV)) / (np.max(imgV) - np.min(imgV))
    imgV = imgV*255

    ###合一
    res = cv2.merge([imgV, imgD, imgV])
    OUT = BFT + '\\' + name
    OUTA = BFTA + '\\' + name
    OUTD = BFTD + '\\' + name
    OUTV = BFTV + '\\' + name
    cv2.imwrite(OUT,res)
    cv2.imwrite(OUTA,imgA)
    cv2.imwrite(OUTD,imgD)
    cv2.imwrite(OUTV,imgV)


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
    
    imgADV = cv2.merge([imgV, imgD, imgV])
    OUTADV = BWADV + '\\' + name
    cv2.imwrite(OUTADV,imgADV)

    imgA = (imgA  - np.min(imgA)) / (np.max(imgA) - np.min(imgA))
    imgA = imgA*255
    
    imgD = (imgD  - np.min(imgD)) / (np.max(imgD) - np.min(imgD))
    imgD = imgD*255
    
    imgV = (imgV - np.min(imgV)) / (np.max(imgV) - np.min(imgV))
    imgV = imgV*255

    res = cv2.merge([imgV, imgD, imgV])
    OUT = BWT + '\\' + name
    OUTA = BWTA + '\\' + name
    OUTD = BWTD + '\\' + name
    OUTV = BWTV + '\\' + name
    cv2.imwrite(OUT,res)
    cv2.imwrite(OUTA,imgA)
    cv2.imwrite(OUTD,imgD)
    cv2.imwrite(OUTV,imgV)
    
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
    
    imgADV = cv2.merge([imgV, imgD, imgV])
    OUTADV = WFADV + '\\' + name
    cv2.imwrite(OUTADV,imgADV)

    imgA = (imgA  - np.min(imgA)) / (np.max(imgA) - np.min(imgA))
    imgA = imgA*255
    
    imgD = (imgD  - np.min(imgD)) / (np.max(imgD) - np.min(imgD))
    imgD = imgD*255
    
    imgV = (imgV - np.min(imgV)) / (np.max(imgV) - np.min(imgV))
    imgV = imgV*255

    res = cv2.merge([imgV, imgD, imgV])
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
    
    imgADV = cv2.merge([imgV, imgD, imgV])
    OUTADV = WWADV + '\\' + name
    cv2.imwrite(OUTADV,imgADV)

    imgA = (imgA  - np.min(imgA)) / (np.max(imgA) - np.min(imgA))
    imgA = imgA*255
    
    imgD = (imgD  - np.min(imgD)) / (np.max(imgD) - np.min(imgD))
    imgD = imgD*255
    
    imgV = (imgV - np.min(imgV)) / (np.max(imgV) - np.min(imgV))
    imgV = imgV*255

    res = cv2.merge([imgV, imgD, imgV])
    OUT = WWT + '\\' + name
    OUTA = WWTA + '\\' + name
    OUTD = WWTD + '\\' + name
    OUTV = WWTV + '\\' + name
    cv2.imwrite(OUT,res)
    cv2.imwrite(OUTA,imgA)
    cv2.imwrite(OUTD,imgD)
    cv2.imwrite(OUTV,imgV)