# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:53:05 2022

@author: jenny
"""
data = []
count = 0

with open('reviews.txt', 'r') as f:
    for line in f:
      data.append(line) 
      count = count + 1
      if count % 1000 ==0:
          print(len(data))
        
print(len(data))
print(data[0])


