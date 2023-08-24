import pandas as pd
from sklearn import preprocessing


C = pd.read_csv(r'test.csv')
no = ['id','label']
drop = C[no]
C = C.drop(no,axis = 1)
nameC = C.columns[:]
data = preprocessing.scale(C,axis=1)
data = pd.DataFrame(data=data,columns=nameC)
data = drop.join(data)
data.to_csv(r'z.csv',encoding='utf_8_sig',index=False)



