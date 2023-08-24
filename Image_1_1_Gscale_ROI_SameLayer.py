import os
import cv2

def MaxROI(di,outpath):
    length = 0
    width = 0
    mid = []
    midname = []
    picname = []
    L = []
    W = []
    names = os.listdir(di)
    numm = len(names)
    for name in names:
        print(di + '\\' + str(name))
        names2 = os.listdir(di + '\\' + str(name) + '\\niijpg')
        maxx = 0
        maxname = 'x'
        for name2 in names2:
            img = cv2.imread(di + '\\' + str(name) + '\\niijpg' + '\\' + str(name2))
            t = img.sum()
            if(t>maxx):
                maxx = t
                maxname = name2
        
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
        l = right - left
        w = down - up
        L.append(l)
        W.append(w)
        print(l,w)
        length += l
        width += w
        picname.append(maxname)
        midname.append(name)
        mid.append([round((left+right)/2,0),round((up+down)/2,0)])
    
    length /= numm
    width /= numm
    return midname,picname,mid,length,width,L,W

def Cut(midname,picname,mid,L,W,di,outpath):
    for k in range(len(midname)):
        img = cv2.imread(di + '\\' + str(midname[k]) + '\\jpg' + '\\' + str(picname[k]))
        midx = mid[k][0]
        midy = mid[k][1]
        length = L[k]*1.05
        width = W[k]*1.05
        left = int(midx) - int(length/2)
        right = int(midx) + int(length/2)
        up = int(midy) - int(width/2)
        down = int(midy) + int(width/2)
        img2 =  img[int(up):int(down),int(left):int(right)]
        out_path = outpath + '\\' + str(midname[k]) + '.jpg'
        cv2.imwrite(out_path,img2)



BFdi = r'BENFUFA'
BFROI = r'BF0'
BWdi = r'BENWEIFUFA'
BWROI = r'BW0'

WFdi = r'WAIFUFA'
WFROI = r'WF0'
WWdi = r'WAIWEIFUFA'
WWROI = r'WW0'

BFA = BFdi + '\\' + 'A'
BFD = BFdi + '\\' + 'D'
BFV = BFdi + '\\' + 'V'

BFROIA = BFROI + '\\' + 'A'
BFROID = BFROI + '\\' + 'D'
BFROIV = BFROI + '\\' + 'V'

BFROIADV = BFROI + '\\' + 'ADV'

BFROIT = BFROI + '\\' + 'T'

BFROITA = BFROI + '\\' + 'TA'
BFROITD = BFROI + '\\' + 'TD'
BFROITV = BFROI + '\\' + 'TV'


BWA = BWdi + '\\' + 'A'
BWD = BWdi + '\\' + 'D'
BWV = BWdi + '\\' + 'V'
BWROIA = BWROI + '\\' + 'A'
BWROID = BWROI + '\\' + 'D'
BWROIV = BWROI + '\\' + 'V'
BWROIADV = BWROI + '\\' + 'ADV'
BWROIT = BWROI + '\\' + 'T'
BWROITA = BWROI + '\\' + 'TA'
BWROITD = BWROI + '\\' + 'TD'
BWROITV = BWROI + '\\' + 'TV'
WFA = WFdi + '\\' + 'A'
WFD = WFdi + '\\' + 'D'
WFV = WFdi + '\\' + 'V'

WFROIA = WFROI + '\\' + 'A'
WFROID = WFROI + '\\' + 'D'
WFROIV = WFROI + '\\' + 'V'
WFROIADV = WFROI + '\\' + 'ADV'
WFROIT = WFROI + '\\' + 'T'
WFROITA = WFROI + '\\' + 'TA'
WFROITD = WFROI + '\\' + 'TD'
WFROITV = WFROI + '\\' + 'TV'
WWA = WWdi + '\\' + 'A'
WWD = WWdi + '\\' + 'D'
WWV = WWdi + '\\' + 'V'

WWROIA = WWROI + '\\' + 'A'
WWROID = WWROI + '\\' + 'D'
WWROIV = WWROI + '\\' + 'V'
WWROIADV = WWROI + '\\' + 'ADV'
WWROIT = WWROI + '\\' + 'T'
WWROITA = WWROI + '\\' + 'TA'
WWROITD = WWROI + '\\' + 'TD'
WWROITV = WWROI + '\\' + 'TV'
###############################################################################  
length = 0
width = 0
BFmidnameA,BFpicnameA,BFmidA,BFlengthA,BFwidthA,BFLA,BFWA = MaxROI(BFA,BFROIA)
BFmidnameD,BFpicnameD,BFmidD,BFlengthD,BFwidthD,BFLD,BFWD = MaxROI(BFD,BFROID)
BFmidnameV,BFpicnameV,BFmidV,BFlengthV,BFwidthV,BFLV,BFWV = MaxROI(BFV,BFROIV)

BWmidnameA,BWpicnameA,BWmidA,BWlengthA,BWwidthA,BWLA,BWWA = MaxROI(BWA,BWROIA)
BWmidnameD,BWpicnameD,BWmidD,BWlengthD,BWwidthD,BWLD,BWWD = MaxROI(BWD,BWROID)
BWmidnameV,BWpicnameV,BWmidV,BWlengthV,BWwidthV,BWLV,BWWV = MaxROI(BWV,BWROIV)

WFmidnameA,WFpicnameA,WFmidA,WFlengthA,WFwidthA,WFLA,WFWA = MaxROI(WFA,WFROIA)
WFmidnameD,WFpicnameD,WFmidD,WFlengthD,WFwidthD,WFLD,WFWD = MaxROI(WFD,WFROID)
WFmidnameV,WFpicnameV,WFmidV,WFlengthV,WFwidthV,WFLV,WFWV = MaxROI(WFV,WFROIV)

WWmidnameA,WWpicnameA,WWmidA,WWlengthA,WWwidthA,WWLA,WWWA = MaxROI(WWA,WWROIA)
WWmidnameD,WWpicnameD,WWmidD,WWlengthD,WWwidthD,WWLD,WWWD = MaxROI(WWD,WWROID)
WWmidnameV,WWpicnameV,WWmidV,WWlengthV,WWwidthV,WWLV,WWWV = MaxROI(WWV,WWROIV)


if(not os.path.exists(BFROI)):
    os.mkdir(BFROI)
    os.mkdir(BFROIA)
    os.mkdir(BFROID)
    os.mkdir(BFROIV)
    os.mkdir(BFROIADV)
    os.mkdir(BFROIT)
    os.mkdir(BFROITA)
    os.mkdir(BFROITD)
    os.mkdir(BFROITV)
if(not os.path.exists(BWROI)):
    os.mkdir(BWROI)
    os.mkdir(BWROIA)
    os.mkdir(BWROID)
    os.mkdir(BWROIV)
    os.mkdir(BWROIADV)
    os.mkdir(BWROIT)
    os.mkdir(BWROITA)
    os.mkdir(BWROITD)
    os.mkdir(BWROITV)
if(not os.path.exists(WFROI)):
    os.mkdir(WFROI)
    os.mkdir(WFROIA)
    os.mkdir(WFROID)
    os.mkdir(WFROIV)
    os.mkdir(WFROIADV)
    os.mkdir(WFROIT)
    os.mkdir(WFROITA)
    os.mkdir(WFROITD)
    os.mkdir(WFROITV)
if(not os.path.exists(WWROI)):
    os.mkdir(WWROI)
    os.mkdir(WWROIA)
    os.mkdir(WWROID)
    os.mkdir(WWROIV)
    os.mkdir(WWROIADV)
    os.mkdir(WWROIT)
    os.mkdir(WWROITA)
    os.mkdir(WWROITD)
    os.mkdir(WWROITV)


Cut(BFmidnameA,BFpicnameA,BFmidA,BFLA,BFWA,BFA,BFROIA)
Cut(BFmidnameA,BFpicnameA,BFmidD,BFLA,BFWA,BFD,BFROID)
Cut(BFmidnameA,BFpicnameA,BFmidV,BFLA,BFWA,BFV,BFROIV)

Cut(BWmidnameA,BWpicnameA,BWmidA,BWLA,BWWA,BWA,BWROIA)
Cut(BWmidnameA,BWpicnameA,BWmidD,BWLA,BWWA,BWD,BWROID)
Cut(BWmidnameA,BWpicnameA,BWmidV,BWLA,BWWA,BWV,BWROIV)

Cut(WFmidnameA,WFpicnameA,WFmidA,WFLA,WFWA,WFA,WFROIA)
Cut(WFmidnameA,WFpicnameA,WFmidD,WFLA,WFWA,WFD,WFROID)
Cut(WFmidnameA,WFpicnameA,WFmidV,WFLA,WFWA,WFV,WFROIV)

Cut(WWmidnameA,WWpicnameA,WWmidA,WWLA,WWWA,WWA,WWROIA)
Cut(WWmidnameA,WWpicnameA,WWmidD,WWLA,WWWA,WWD,WWROID)
Cut(WWmidnameA,WWpicnameA,WWmidV,WWLA,WWWA,WWV,WWROIV)



############################################################

def Cut0(midname,picname,mid,L,W,di,outpath):
    for k in range(len(midname)):
        img = cv2.imread(di + '\\' + str(midname[k]) + '\\orijpg' + '\\' + str(picname[k]))
        midx = mid[k][0]
        midy = mid[k][1]
        length = L[k]*1.05
        width = W[k]*1.05
        left = int(midx) - int(length/2)
        right = int(midx) + int(length/2)
        up = int(midy) - int(width/2)
        down = int(midy) + int(width/2)
        img2 =  img[int(up):int(down),int(left):int(right)]
        out_path = outpath + '\\' + str(midname[k]) + '.jpg'
        cv2.imwrite(out_path,img2)

BFdi = r'BENFUFA'
BFROI = r'BF0'
BWdi = r'BENWEIFUFA'
BWROI = r'BW0'

WFdi = r'WAIFUFA'
WFROI = r'WF0'
WWdi = r'WAIWEIFUFA'
WWROI = r'WW0'

BFA = BFdi + '\\' + 'A'
BFD = BFdi + '\\' + 'D'
BFV = BFdi + '\\' + 'V'
BFROIA = BFROI + '\\' + 'A'
BFROID = BFROI + '\\' + 'D'
BFROIV = BFROI + '\\' + 'V'
BFROIADV = BFROI + '\\' + 'ADV'
BFROIT = BFROI + '\\' + 'T'
BFROITA = BFROI + '\\' + 'TA'
BFROITD = BFROI + '\\' + 'TD'
BFROITV = BFROI + '\\' + 'TV'


BWA = BWdi + '\\' + 'A'
BWD = BWdi + '\\' + 'D'
BWV = BWdi + '\\' + 'V'
BWROIA = BWROI + '\\' + 'A'
BWROID = BWROI + '\\' + 'D'
BWROIV = BWROI + '\\' + 'V'
BWROIADV = BWROI + '\\' + 'ADV'
BWROIT = BWROI + '\\' + 'T'
BWROITA = BWROI + '\\' + 'TA'
BWROITD = BWROI + '\\' + 'TD'
BWROITV = BWROI + '\\' + 'TV'
WFA = WFdi + '\\' + 'A'
WFD = WFdi + '\\' + 'D'
WFV = WFdi + '\\' + 'V'

WFROIA = WFROI + '\\' + 'A'
WFROID = WFROI + '\\' + 'D'
WFROIV = WFROI + '\\' + 'V'
WFROIADV = WFROI + '\\' + 'ADV'
WFROIT = WFROI + '\\' + 'T'
WFROITA = WFROI + '\\' + 'TA'
WFROITD = WFROI + '\\' + 'TD'
WFROITV = WFROI + '\\' + 'TV'
WWA = WWdi + '\\' + 'A'
WWD = WWdi + '\\' + 'D'
WWV = WWdi + '\\' + 'V'

WWROIA = WWROI + '\\' + 'A'
WWROID = WWROI + '\\' + 'D'
WWROIV = WWROI + '\\' + 'V'
WWROIADV = WWROI + '\\' + 'ADV'
WWROIT = WWROI + '\\' + 'T'
WWROITA = WWROI + '\\' + 'TA'
WWROITD = WWROI + '\\' + 'TD'
WWROITV = WWROI + '\\' + 'TV'

if(not os.path.exists(BFROI)):
    os.mkdir(BFROI)
    os.mkdir(BFROIA)
    os.mkdir(BFROID)
    os.mkdir(BFROIV)
    os.mkdir(BFROIADV)
    os.mkdir(BFROIT)
    os.mkdir(BFROITA)
    os.mkdir(BFROITD)
    os.mkdir(BFROITV)
if(not os.path.exists(BWROI)):
    os.mkdir(BWROI)
    os.mkdir(BWROIA)
    os.mkdir(BWROID)
    os.mkdir(BWROIV)
    os.mkdir(BWROIADV)
    os.mkdir(BWROIT)
    os.mkdir(BWROITA)
    os.mkdir(BWROITD)
    os.mkdir(BWROITV)
if(not os.path.exists(WFROI)):
    os.mkdir(WFROI)
    os.mkdir(WFROIA)
    os.mkdir(WFROID)
    os.mkdir(WFROIV)
    os.mkdir(WFROIADV)
    os.mkdir(WFROIT)
    os.mkdir(WFROITA)
    os.mkdir(WFROITD)
    os.mkdir(WFROITV)
if(not os.path.exists(WWROI)):
    os.mkdir(WWROI)
    os.mkdir(WWROIA)
    os.mkdir(WWROID)
    os.mkdir(WWROIV)
    os.mkdir(WWROIADV)
    os.mkdir(WWROIT)
    os.mkdir(WWROITA)
    os.mkdir(WWROITD)
    os.mkdir(WWROITV)


Cut0(BFmidnameA,BFpicnameA,BFmidA,BFLA,BFWA,BFA,BFROIA)
Cut0(BFmidnameA,BFpicnameA,BFmidD,BFLA,BFWA,BFD,BFROID)
Cut0(BFmidnameA,BFpicnameA,BFmidV,BFLA,BFWA,BFV,BFROIV)

Cut0(BWmidnameA,BWpicnameA,BWmidA,BWLA,BWWA,BWA,BWROIA)
Cut0(BWmidnameA,BWpicnameA,BWmidD,BWLA,BWWA,BWD,BWROID)
Cut0(BWmidnameA,BWpicnameA,BWmidV,BWLA,BWWA,BWV,BWROIV)

Cut0(WFmidnameA,WFpicnameA,WFmidA,WFLA,WFWA,WFA,WFROIA)
Cut0(WFmidnameA,WFpicnameA,WFmidD,WFLA,WFWA,WFD,WFROID)
Cut0(WFmidnameA,WFpicnameA,WFmidV,WFLA,WFWA,WFV,WFROIV)

Cut0(WWmidnameA,WWpicnameA,WWmidA,WWLA,WWWA,WWA,WWROIA)
Cut0(WWmidnameA,WWpicnameA,WWmidD,WWLA,WWWA,WWD,WWROID)
Cut0(WWmidnameA,WWpicnameA,WWmidV,WWLA,WWWA,WWV,WWROIV)