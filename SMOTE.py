import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE


if __name__ == '__main__':
    data = pd.read_csv(r'test.csv')
    label = data['label'].values
    no = ['label','ID']
    data = data.drop(no, axis=1)
    name = data.columns[:]
    smo = SMOTE(random_state=21)
    data, label = smo.fit_resample(np.array(data),np.array(label))
    
    data = pd.DataFrame(data = data,columns=name)
    idnum = []
    for i in range(len(label)):
        idnum.append(i)
    ID = pd.DataFrame(data = idnum,columns=['id'])
    label = pd.DataFrame(data = label,columns=['label'])
    
    data = ID.join(label).join(data)
    name = data.columns[:]
    pd.DataFrame(columns=name,data=data).to_csv(r'smote.csv',encoding='utf_8_sig',index = False)

    
    