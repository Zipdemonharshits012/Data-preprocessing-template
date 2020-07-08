#Template for EDA by Harshit Soni 

"""Importing Basic Libraries"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



"""Reading data as file from our system using pandas"""
dataset=pd.read_csv('Data.csv')
print(dataset)
print(dataset.head(8),"\n\n\n\n")
print(dataset.describe())#tells mean 25p 50p and max

x=dataset.iloc[:,:3].values
y=dataset.iloc[:,3:].values
#x=pd.DataFrame(x) # do not use while using simple imputer 
#y=pd.DataFrame(y)
print(x,"\n\n")
print(y,"\n\n ")




'''"""Missing data """
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy="mean")
x[:,1:3]=imputer.fit_transform(x[:,1:3])
#y=imputer.fit_transform(y)
print(x,"\n \n")'''




'''"""Handling Categorical Data and Encoding it"""
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x= np.array(ct.fit_transform(x))'''

'''Encoding the Dependent Variable"""
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)'''




'''#Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)
'''




'''#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])'''




