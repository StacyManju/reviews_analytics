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
print('檔案讀取完成,共有', len(data), '筆資料')

sumlen = 0
for LongLine in data:
    sumlen = sumlen +len(LongLine)

print('留言的平均長度是', sumlen/len(data))
     

