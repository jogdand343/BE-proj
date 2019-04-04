# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)

def predict(x,d):
    kw_list = [x]
    pytrends.build_payload(kw_list, cat=0, timeframe='2014-01-06 2018-12-31', geo='', gprop='')
    
    dataset = pytrends.interest_over_time()
    #print (dataset)
    
    Y = dataset.iloc[:, :-1].values
    #print (Y)
    #len (Y)
    
    A =  [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
    
    X = np.asarray(A)
    
    #print (X)
    #len (X)
    
    def chunks(l, n):
  
        for i in range(0, len(l), n):
        
            yield l[i:i+n]
            
    E=list(chunks(Y, 52))

    newDataset = []
    
    L = E[0]
    M = E[1]
    N = E[2]
    O = E[3]
    P = E[4] 
    
    for i in range(0,52):
        newDataset.append((np.mean(L[i])+ np.mean(M[i])+np.mean(N[i])+np.mean(O[i])+np.mean(P[i]))/5) 
    
    #len(newDataset)
    finalDataset = np.reshape(newDataset, (-1,1))
    X = np.reshape(X,(-1,1))

    #print(finalDataset)
    #len (finalDataset)
    #len (X)
        
    from sklearn.linear_model import LinearRegression
    lin_reg = LinearRegression()
    lin_reg.fit(finalDataset, X)
    
    # Fitting Polynomial Regression to the dataset
    from sklearn.preprocessing import PolynomialFeatures
    poly_reg = PolynomialFeatures(degree = 9)
    X_poly = poly_reg.fit_transform(X)
    poly_reg.fit(X_poly, finalDataset)
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(X_poly, finalDataset)

    """# Visualising the Linear Regression results
    #plt.scatter(X, Y, color = 'red')
    #plt.plot(X, lin_reg.predict(X), color = 'blue')
    #plt.title('Truth or Bluff (Linear Regression)')
    #plt.xlabel('Interest')
    plt.ylabel('Week')
    plt.show()"""
    
    X_grid = np.arange(min(X), max(X), 0.01)
    X_grid = X_grid.reshape((len(X_grid), 1))
    plt.scatter(X, finalDataset, color = 'red')
    plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
    plt.title('Truth or Bluff (Polynomial Regression)')
    plt.xlabel('Week Number')
    plt.ylabel('Interest')
    plt.show()
    
    
    t = lin_reg_2.predict(poly_reg.fit_transform([[d]]))
    t = t.astype(np.float64)
    s = finalDataset[[int(d)]]
    p = t[0]
    print(p)
    print(s)  
