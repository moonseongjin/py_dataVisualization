# 1월과 8월의 데이터를 히스토그램으로 시각화하기

import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data) 

aug = []
jan = []


for row in data:
    month = row[0].split('-')[1] # -로 구분된 값 중 2번째 값을 month에 저장
    if row[-1] != '' :
        if month == '08':
            aug.append(float(row[-1]))
        if month == '01':
            jan.append(float(row[-1]))
        
plt.hist(aug, bins=100, color = 'r', label='Aug')        
plt.hist(jan, bins=100, color = 'b', label='Jan')

plt.legend()
plt.show()