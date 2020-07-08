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




"""Missing data """
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy="mean")
x[:,1:3]=imputer.fit_transform(x[:,1:3])
#y=imputer.fit_transform(y)
print(x,"\n \n")




"""Handling Categorical Data and Encoding it"""
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
le=LabelEncoder()
x[:,0]=le.fit_transform(x[:,0])
y[:,0]=le.fit_transform(y[:,0])




