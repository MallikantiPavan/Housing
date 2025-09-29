import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score
import joblib

train=pd.read_csv(r'C:\Users\pavan\Downloads\house-prices-advanced-regression-techniques\train.csv')
test=pd.read_csv(r'C:\Users\pavan\Downloads\house-prices-advanced-regression-techniques\test.csv')

train=train.drop(['LotFrontage'],axis=1)
test=test.drop(['LotFrontage'],axis=1)
train=pd.get_dummies(train,columns=['MSZoning'])
test_df=pd.get_dummies(test,columns=['MSZoning'])

drop_cols=['Id','PoolQC','PoolArea']
train=train.drop(columns=drop_cols,axis=1)
test_df=test_df.drop(columns=drop_cols,axis=1)

cat_columns=train.select_dtypes(include=['object']).columns

train=pd.get_dummies(train,columns=cat_columns)
test_df=pd.get_dummies(test,columns=cat_columns)



x=train.drop(['SalePrice'],axis=1)
y=train['SalePrice']

test_df=test_df.reindex(columns=x.columns,fill_value=0)

num_cols=x.select_dtypes(include=[np.number]).columns
model_imp=SimpleImputer(strategy='median')
x[num_cols]=model_imp.fit_transform(x[num_cols])
test_df[num_cols]=model_imp.fit_transform(test_df[num_cols])



x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42)

model=LinearRegression()
model.fit(x_train,y_train)
y_fit=model.predict(x_test)
# print("r2:",r2_score(y_fit,y_test))
joblib.dump(model,"housing_model.pkl")
print("model dumped successfully")