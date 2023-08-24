import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso


inputfile = r""
data = pd.read_csv(inputfile)

lasso = Lasso(0.001)
y = data['label']
data2 = data.drop(columns = ['label'])
lasso.fit(data2,y)
print(np.round(lasso.coef_,5))


print(np.sum(lasso.coef_ != 0))
mask = lasso.coef_ != 0
print(mask)

outputfile = r'LASSO.csv'
new_reg_data = data2.iloc[:, mask]
new_reg_data.to_csv(outputfile)
print(new_reg_data.shape)
