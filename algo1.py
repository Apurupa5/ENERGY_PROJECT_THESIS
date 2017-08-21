# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 20:58:18 2017
@author: NB VENKATESHWARULU
"""

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import time

def S1_scorealgo(k,power_values):
    scores=[]
    index=0;
    for power in power_values:
        i=1
        signed_leftdist=[]
        signed_rightdist=[]
        while i<=k:
            if  index-i <0 or index+i >=len(power_values):
                break
            signed_leftdist.append(power-power_values[index-i])
            signed_rightdist.append(power-power_values[index+i])
            i=i+1
        if len(signed_leftdist)==0 or len(signed_rightdist)==0:
            scores.append(0)
        else:
            max_left=max(signed_leftdist)
            max_right=max(signed_rightdist)
            scores.append((max_left+max_right)/2)
       # print(scores)
        index=index+1

    scores_array=np.array(scores)
    mean_scores=np.mean(scores_array)
    std_dev=np.std(scores_array)
    print(mean_scores)
    print(std_dev)
    print(scores)
    return (scores,mean_scores,std_dev)


def S5_scorealgo(k,power_values,threshold):
    print("Using S5 algo:")
    for i in range(k,len(power_values)):
        window=power_values[(i-k-1):(i+k+1)]
        mean_window=np.mean(window)
        stddev_window=np.std(window)
        #print(mean_window)
        #print(stddev_window)
        #print("power", power_values[i],abs(power_values[i]-mean_window),threshold*stddev_window)
        if power_values[i]>=mean_window and abs(power_values[i]-mean_window)>=threshold*stddev_window :
             print("Time",timestamp_values[i],"Value:",power_values[i])
            
  
def printpeaks(h,scores,mean_scores,std_dev):
    index=0
    print("Following are peaks:\n")
    for score in scores:
      
        if score>0 and (score-mean_scores)>h*std_dev:
            print("Time",timestamp_values[index],"Value:",power_values[index])
        index=index+1  
             
      
#df = pd.read_csv('apFac_502.csv')
df = pd.read_csv('day2.csv')
print (df)

#df['timestamp'] = df['timestamp'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))
df['timestamp'] = df['timestamp'].map(lambda x: datetime.strptime(str(x), '%m/%d/%Y %H:%M'))
timestamp_values = df['timestamp']
power_values = df['power']
plt.plot(timestamp_values,power_values)
plt.gcf().autofmt_xdate()
plt.show() #plotting graph

#Implementing one of the methods in Palshinkar
k=4
h=2
start = time.time()
scores,mean,stddev=S1_scorealgo(k,power_values)
printpeaks(h,scores,mean,stddev)
print ("Time for S1", time.time() - start)

start = time.time()
S5_scorealgo(5,power_values,2)
print ("Time for S5", time.time() - start)
