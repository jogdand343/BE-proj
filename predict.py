# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
pip install pytrends
pip install matplotlib
pip install -U scikit-learn scipy matplotlib

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from pytrends.request import TrendReq

kw_list = ["Disneyland florida"]
pytrends.build_payload(kw_list, cat=0, timeframe='2018-01-01 2018-12-31', geo='', gprop='')

dataset = pytrends.interest_over_time()
print (dataset)

Y = dataset.iloc[:, :-1].values
print (Y)
len (Y)

A =  [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

X = np.asarray(A)

print (X)
len (X)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(Y, X)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 7)
Y_poly = poly_reg.fit_transform(Y)
poly_reg.fit(Y_poly, X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(Y_poly, X)

# Visualising the Linear Regression results
plt.scatter(X, Y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Interest')
plt.ylabel('Week')
plt.show()

Y_grid = np.arange(min(Y), max(Y), 0.01)
Y_grid = Y_grid.reshape((len(Y_grid), 1))
plt.scatter(Y, X, color = 'red')
plt.plot(Y_grid, lin_reg_2.predict(poly_reg.fit_transform(Y_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Interest')
plt.ylabel('Week')
plt.show()

  
