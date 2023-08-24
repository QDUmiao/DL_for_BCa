import os
from shutil import copyfile

DATA = r'DATAD'
TEST = r'TESTD'
BF = r'BF'
BW = r'BW'
WF = r'WF'
WW = r'WW'
DATAFUFA = DATA + '\\' + 'FUFA'
DATAWEIFUFA = DATA + '\\' + 'WEIFUFA'
TESTFUFA = TEST + '\\' + 'FUFA'
TESTWEIFUFA = TEST + '\\' + 'WEIFUFA'
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

if(not os.path.exists(DATA)):
    os.mkdir(DATA)
    os.mkdir(DATAFUFA)
    os.mkdir(DATAWEIFUFA)
if(not os.path.exists(TEST)):
    os.mkdir(TEST)
    os.mkdir(TESTFUFA)
    os.mkdir(TESTWEIFUFA)
    
names = os.listdir(BFT)
for name in names:
    source = BFT + '\\' + name
    target = DATAFUFA + '\\' + name
    copyfile(source, target)
    
names = os.listdir(BWT)
for name in names:   
    source = BWT + '\\' + name
    target = DATAWEIFUFA + '\\' + name
    copyfile(source, target)
    
names = os.listdir(WFT)
for name in names:    
    source = WFT + '\\' + name
    target = TESTFUFA + '\\' + name
    copyfile(source, target)
names = os.listdir(WWT)
for name in names:   
    source = WWT + '\\' + name
    target = TESTWEIFUFA + '\\' + name
    copyfile(source, target)
