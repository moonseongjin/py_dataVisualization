"""
# 꺾은선 그래프 비교
import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []

name = input('궁금한 동네를 입력해주세요:')
for row in data :
    if name in row[0] :
        for i in range(3,104) :
            m.append(int(row[i]))      # 남성 데이터 저장하기
            f.append(int(row[i+103]))  # 여성 데이터 저장하기    
        break
        
import matplotlib.pyplot as plt
plt.plot(m, label='Male')
plt.plot(f, label='Female')
plt.legend()
plt.show()

===========================================================================
# 막대 그래프
import csv
f = open('gender.csv')
data = csv.reader(f)
result = []

name = input('궁금한 동네를 입력해주세요:')
for row in data :
    if name in row[0] :
        for i in range(3,104) :
           result.append(int(row[i]) - int(row[i+103])) 
        break
        
import matplotlib.pyplot as plt
plt.bar(range(101),result)
plt.show()

===========================================================================
# 버블 차트로 표현하기
import matplotlib.pyplot as plt
import random

x= []
y= []
size = []

for i in range(100):
    x.append(random.randint(50,100))
    y.append(random.randint(50,100))
    size.append(random.randint(10,100))
plt.scatter(x,y, s=size, c=size, cmap='jet', alpha=0.7) # 0에 가까울 수록 투명
plt.colorbar()
plt.show()

"""

# 제주도의 연령대별 성별 비율을 산점도로 표현하기

import csv
import math

f = open('gender.csv')
data = csv.reader(f)
m = []
f = []
size = []

name = input('궁금한 동네를 입력해주세요: ')
for row in data:
    if name in row[0]:
        for i in range(3,104):
            m.append(int(row[i]))
            f.append(int(row[i+103]))
            size.append(math.sqrt(int(row[i])+int(row[i+103]))) # 점의 크기
        break
        
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', family = 'Malgun Gothic')
plt.figure(figsize=(10,5), dpi=300)
plt.title(name+' 지역의 성별 인구 그래프') 
plt.scatter(m,f, s = size, c=range(101),  alpha=0.5, cmap='jet') #컬러맵 적용
plt.colorbar()
plt.plot(range(max(m)),range(max(m)),'g') # 추세선 추가
plt.xlabel('남성 인구수')
plt.ylabel('여성 인구수')
plt.show()