# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:57:41 2017

@author: NB VENKATESHWARULU
"""
# Implementing by two smoothings followed by a peak detection
import numpy as np
import matplotlib.pyplot as plt
import time

from datetime import datetime
import pandas as pd

def smooth(lag,power_values):
    smoothed_values = np.zeros(len(power_values))
   
    for i in range(lag/2, len(power_values)):
        smoothed_values[i]=np.mean(power_values[(i-lag/2):(i+lag/2)+1])
        
    return smoothed_values
def printpeaks(scores,x):
    std=np.std(scores)
    print("Score",scores)
    print(std)
    index=0
    print(x*std)
    print("Following are peaks:\n")
    """
    for score in scores:
       print("Score", score, index)
       if score>=x*std:
          
          print("Time",timestamp_values[index],"Value:",power_values[index])
       index=index+1  
    """
    for score in scores:
      # print("Score", score, index)
       if score>=x*std and scores[index-1]<=scores[index] and scores[index]>=scores[index+1]:
          
          print("Time",timestamp_values[index],"Value:",power_values[index])
       index=index+1  


def adaptive(scores,k):
   
    avg=np.mean(scores)
    max=np.max(scores)
    sum=0
    for score in scores:
        sum=sum+abs(score-avg)
    abs_dev=sum/len(scores)
    threshold=(max+avg)/2 + k*abs_dev
  
    print("Following are peaks by adaptive:\n")
    index=0
    for score in scores:
      # print("Score", score, index)
       if score>=threshold:
          
          print("Time",timestamp_values[index],"Value:",power_values[index])
       index=index+1  

           
#df = pd.read_csv('sample2.csv')
#df = pd.read_csv('apFac_502.csv')
df = pd.read_csv('day2.csv')
#print (df)
#df['timestamp'] = df['timestamp'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))
df['timestamp'] = df['timestamp'].map(lambda x: datetime.strptime(str(x), '%m/%d/%Y %H:%M'))
timestamp_values = df['timestamp']
power_values = df['power']
plt.plot(timestamp_values,power_values)
plt.gcf().autofmt_xdate()
plt.show() 
start = time.time()
lag=3
smoothed_values=smooth(lag,power_values)
user_constant=1.5
#printpeaks(smoothed_values,user_constant)

plt.plot(timestamp_values,smoothed_values)
plt.gcf().autofmt_xdate()
plt.show() 

smoothed_values=smooth(lag,smoothed_values)
plt.plot(timestamp_values,smoothed_values)
plt.gcf().autofmt_xdate()
plt.show() 

printpeaks(smoothed_values,user_constant)
print ("Time for Algo3", time.time() - start)

adaptive(smoothed_values,0.5)


"""
eg=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,34,1,1,1]
print(np.mean(eg[17:22]))
s=smooth(5,eg)
for l in s:
    print(l)
"""