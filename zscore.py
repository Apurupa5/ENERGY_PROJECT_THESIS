# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:44:13 2017

@author: NB VENKATESHWARULU
"""
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


def z_scorealgo(lag,threshold,influence,power_values):
   
    scores=[0]*len(power_values)
    filteredY = np.array(power_values)

    for i in range(lag,len(power_values)):
        moving_window=filteredY[(i-lag):i]
        moving_mean=np.mean(moving_window)
        moving_stddev=np.std(moving_window)
        if abs(power_values[i] -moving_mean) > threshold * moving_stddev:
            scores[i]=1
            filteredY[i]= influence * power_values[i] + (1 - influence) * filteredY[i-1]
          
        else:
            scores[i] = 0
            filteredY[i]= power_values[i]
    return scores 
    

def printpeaks(scores):
   
    index=0
    print("Following are peaks:\n")
    for score in scores:
      
       if score==1:
           print("Time",timestamp_values[index],"Value:",power_values[index])
       index=index+1  
             
      
#df = pd.read_csv('apFac_502.csv')
df = pd.read_csv('day4.csv')
print (df)

#df['timestamp'] = df['timestamp'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))
df['timestamp'] = df['timestamp'].map(lambda x: datetime.strptime(str(x), '%m/%d/%Y %H:%M'))
timestamp_values = df['timestamp']
power_values = df['power']
plt.plot(timestamp_values,power_values)
plt.gcf().autofmt_xdate()
plt.show() #plotting graph

#Implementing one of the methods in Palshinkar
lag=3
threshold=3
influence=0
print(np.mean(power_values))
print(np.std(power_values))
scores=z_scorealgo(lag,threshold,influence,power_values)
print(np.mean(scores))
print(np.std(scores))
printpeaks(scores)
