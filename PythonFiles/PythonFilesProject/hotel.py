import numpy as np
import pandas as pd

def search(x):
    datasetHotel = pd.read_csv('test.csv')
    datasetHotel.drop(["Unnamed: 4","Unnamed: 5","Unnamed: 6","Unnamed: 7","Unnamed: 8","Unnamed: 9","Unnamed: 10","Unnamed: 11","Unnamed: 12","Unnamed: 13","Unnamed: 14","Unnamed: 15","Unnamed: 16","Unnamed: 17","Unnamed: 18","Unnamed: 19","Unnamed: 20","Unnamed: 21","Unnamed: 22","Unnamed: 23","Unnamed: 24","Unnamed: 25","Unnamed: 26"], axis = 1, inplace = True) 
    datasetHotel.drop(["hotel_star_rating", "property_name","state"], axis = 1, inplace = True)
    datasetHotel.drop(["tad_stay_review_rating"], axis = 1, inplace = True)
    datasetHotel.drop(["property_id"], axis = 1, inplace = True)
    newDatasetHotel = datasetHotel[np.isfinite(datasetHotel['tad_review_count'])]
    #x=input("Enter the City Name")
    
    print (newDatasetHotel[newDatasetHotel["city"] == x])
    a = newDatasetHotel[newDatasetHotel["city"] == x]
    print("Average rating in %s is" %x)
    print(np.mean(a.iloc[:, 2].values))
