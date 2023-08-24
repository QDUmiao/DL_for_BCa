import pymrmr
import pandas as pd

import time

path = r"test.csv"
print(path)
Z = pd.read_csv(path)
print(Z)


time.sleep(1)
MR = pymrmr.mRMR(Z, 'MIQ', 30)



###############################################################################


Z = pd.read_csv(r"TEST.csv")

T = ['ID','NAME','Label','Source']

for i in MR:
    T.append(i)
    
Z2 = Z[T]

Z2.to_csv(r'MRMR.csv',encoding='utf_8_sig')