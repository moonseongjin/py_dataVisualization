"""
# 박스 플롯 (Box plot)
최소값
제 1사분위 수 (Q1)
제 2사분위 수 또는 중위수 (Q2)
제 3사분위 수 (Q3)
최대값
===========================================
# 박스 플롯
import matplotlib.pyplot as plt
import random

result = []
for i in range(13):
    result.append(random.randint(1,1000))
print(sorted(result))

plt.boxplot(result)
plt.show()
===========================================
# 박스 플롯 값 출력
import matplotlib.pyplot as plt
import random
import numpy as np

result = np.array(result)

print("1/4:" + str(np.percentile(result,25)))
print("2/4:" + str(np.percentile(result,50)))
print("3/4:" + str(np.percentile(result,75)))
print("4/4:" + str(np.percentile(result,100)))

plt.boxplot(result)
plt.show()
"""

#8월 일별 기온 데이터를 박스 플롯으로 표현하기
import matplotlib.pyplot as plt
import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)

day = []
for i in range(31):
    day.append([])
    
for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '08':
            # 최고 기온 값 저장
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))
plt.style.use('ggplot') # 그래프 스타일
plt.figure(figsize=(10,5),dpi=300) # 가로 10, 세로 5 해상도를 300으로 설정
plt.boxplot(day, showfliers=False) # 아웃라이어 값 생략

plt.show()