import numpy as np
import os
import pandas as pd
import radiomics.featureextractor as featureextractor
import SimpleITK as sitk

def wavelet(imageFile,maskFile,para_name):#提取特征
    origin_img=sitk.ReadImage(imageFile)
    w=sitk.ReadImage(maskFile)
    origin=origin_img.GetOrigin()
    w.SetOrigin(origin)
    direction=origin_img.GetDirection()
    w.SetDirection(direction)
    spacing=origin_img.GetSpacing()
    w.SetSpacing(spacing)
    sitk.WriteImage(w,maskFile)
    extractor = featureextractor.RadiomicsFeatureExtractor(para_name)
    extractor.enableImageTypes() 
    featureVector = extractor.execute(imageFile, maskFile)
    feature=[]
    fname=[]
    for featureName in featureVector.keys():
        fname.append(featureName)
        feature.append(str(featureVector[featureName]))
    lie = np.array(fname).shape[0]
    fname=np.array(fname).reshape(1,lie)
    fname=list(fname)
    feature=np.array(feature).reshape(1,lie)
    feature=list(feature)
    return fname,feature
    
def fwgetfeature(file_path,s):
    imageFile=file_path+'\Ori.nrrd'
    names = os.listdir(file_path)
    for name in names:
        if(str(name) != 'Ori.nrrd' and (not os.path.isdir(file_path+str(name)))):
            ss = str(name)
            break
    maskFile=file_path+'\\' + ss
    para_name = 'Params2.yaml'
    return wavelet(imageFile,maskFile,para_name)

def iccgetfeature(file_path,s):
    imageFile=file_path+'\Ori.nrrd'
    maskFile=file_path+'\\' + s + '.nii'
    para_name = 'Params2.yaml'
    return wavelet(imageFile,maskFile,para_name)
def DcmToNrrd(file_path,s):
    file_path2=file_path
    file_path+=s
    dcms_name = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(file_path)
    dcms_read = sitk.ImageSeriesReader()
    dcms_read.SetFileNames(dcms_name)
    dcms_series = dcms_read.Execute()
    sitk.WriteImage(dcms_series,file_path2+'Ori'+'.nrrd')

def wDcmToNrrd(file_path,s):
    file_path2=file_path
    file_path += s
    dcms_name = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(file_path)
    dcms_read = sitk.ImageSeriesReader()
    dcms_read.SetFileNames(dcms_name)
    dcms_series = dcms_read.Execute()
    sitk.WriteImage(dcms_series,file_path2+'Ori'+'.nrrd')


def fun(di,s):

        DcmToNrrd(di,s)
        fname,feature = fwgetfeature(di,s)
        return fname,feature


def wfun(di,s):

        wDcmToNrrd(di,s)
        fname,feature = fwgetfeature(di,s)
        return fname,feature


source = ""
FFYES = 1
FF = r'FUFA'
OUT = FF[:-4]
A = FF + '\A'
V = FF + '\V'
D = FF + '\D'
WFFYES = 1
WFF = r'WEIFUFA'
WA = WFF + '\A'
WD = WFF + '\D'
WV = WFF + '\V'
ERROR = []
        

        
summ = 0
icc = []
names = os.listdir(WA)
for name in names:
    icc.append(name)
    summ += 1

num = 0
Featureicc = []
fnameicc = []
featureicc = []
for name in icc:
    print(name)
    s = str(name)
    try:
        WAA = WA + '\\'  + s + '\\'
        na,fa = wfun(WAA,'DICOM')
        WVV = WV + '\\'  + s + '\\'
        nv,fv = wfun(WVV,'DICOM')
        WDD = WD + '\\'  + s + '\\'
        nd,fd = wfun(WDD,'DICOM')
        
        num += 1
        
        if(len(fnameicc) == 0):
            fnameicc.append('ID')
            fnameicc.append('NAME')
            fnameicc.append('SOURCE')
            fnameicc.append('LABEL')
            
            for i in na:
                for j in list(i):
                    fnameicc.append('A_'+j)
            for i in nv:
                for j in list(i):
                    fnameicc.append('V_'+j)
            for i in nd:
                for j in list(i):
                    fnameicc.append('D_'+j)
        
        
        s1 = ""
        s2 = ""
        for i in s:
            if(i.isdigit()):
                s1 += i
            elif(i.isalpha()):
                s2 += i
        
        featureicc = []
        Featureicc.append(s1)
        Featureicc.append(s2)
        Featureicc.append(source)
        Featureicc.append('0')
        for i in fa:
            for j in list(i):
                featureicc.append(j)
        for i in fv:
            for j in list(i):
                featureicc.append(j)
        for i in fd:
            for j in list(i):
                featureicc.append(j)
        
        
        for i in featureicc:
            Featureicc.append(i)
        
        FeatureiccX = Featureicc
        FeatureiccX = list(np.array(FeatureiccX).reshape(num,int(np.array(FeatureiccX).shape[0]/num)))
        pd.DataFrame(columns=fnameicc,data=FeatureiccX).to_csv(OUT+'\X.csv',encoding='utf_8_sig')
    
        print(round(num*100/summ,0),"%")
    except:
        ERROR.append(['XX',name])
        pd.DataFrame(columns=['Type','Name'],data=ERROR).to_csv(OUT+'\ERRORDATA.csv')