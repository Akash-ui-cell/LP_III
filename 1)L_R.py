  # -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:35:40 2022

@author: DELL
"""



import matplotlib.pyplot as plt
import pandas as pd

# Read Dataset
dataset=pd.read_csv("1)Book1.csv")
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values

# X=[[10],[30],[50],[96],[15],[36],[11],[100]]
# y=[20,40,60,106,25,46,21,140]


# Import the Linear Regression and Create object of it
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,y)
Accuracy=regressor.score(X, y)*100
print("Accuracy :")
print(Accuracy)

# Predict the value using Regressor Object
y_pred=regressor.predict([[10]])
print(y_pred)

# Take user input
hours=int(input('Enter the no of hours:'))
eq=regressor.coef_*hours+regressor.intercept_
print(eq)

# plot graph
plt.scatter(X,y)
plt.plot(X,regressor.predict(X))
plt.show()