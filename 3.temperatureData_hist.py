"""
# 히스토 그램 hist()

import matplotlib.pyplot as plt
plt.hist([1,1,2,3,4,5,6,6,7,8,10])
plt.show()
==================================================================
# 주사위 시뮬레이션 히스토그램으로 표현
import matplotlib.pyplot as plt
import random

dice = []
for i in range(5):
    dice.append(random.randint(1,6))
plt.hist(dice, bins=6) # bins는 가로축의 구간 개수를 설정하는 속성
plt.show()
==================================================================

# 기온 데이터를 히스토그램으로 표현하기
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data) 
result = []

for row in data:
    if row[-1] !='':
        result.append(float(row[-1]))
plt.hist(result, bins=100, color='r')
plt.show()
"""

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