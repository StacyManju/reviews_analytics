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
     
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言有提到good')
print(good[0])

good2 = [d for d in data if 'good' in d]
print(good2)

good3 = [1 for d in data if 'good' in d]
print(good3)

bad = ['bad' in d for d in data]
print(bad)
