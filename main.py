# importing the library

import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

# importing the data set

dataset = pd.read_csv("Data.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
#
print(x)
print(y)


print(".........................>>>>>>>>>>>>>>>>>")

# taking care of missing data

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

print(x)
print(y)

# Encoding the categorical data
# Encoding the Independent Variable

ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [0])], remainder='passthrough')

print("this line ")
x = np.array(ct.fit_transform(x))

print("....>>>>>><<<<>>>>>>>")
print(x)

# Encoding the dependent variable
le = LabelEncoder()
y = le.fit_transform(y)

print("yyyyyyyyyyyyyyyyyyyyyyyyyy")
print(y)

# Splitting the dataset into the Training set and Test set

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
print(x_train)
print(x_test)
print(y_train)
print(y_test)

# feature Scaling

print("scale...................................>>>>>>>>>>>>>>>>>>")
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.fit_transform(x_test[:, 3:])

print("scale12222...................................>>>>>>>>>>>>>>>>>>")

print(x_train)
print(x_test)
