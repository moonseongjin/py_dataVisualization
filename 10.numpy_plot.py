"""
# 다양한 그래프 그리기 (꺾은선 그래프)
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()
=============================================
# 다양한 그래프 그리기 (꺾은선 그래프)
import matplotlib.pyplot as plt
t=[]
p2=[]
p3=[]

for i in range(0,50,2):
    t.append(i / 10)
    p2.append((i/10)**2)
    p3.append((i/10)**3)
plt.plot(t,t,'r--',t,p2,'bs',t,p3,'g^')
plt.show()

=============================================
# 다양한 그래프 그리기 (히스토그램)
import matplotlib.pyplot as plt
import numpy as np

dice = np.random.choice(6,10)

plt.hist(dice, bins=6)
plt.show()

=============================================
# 다양한 그래프 그리기 (히스토그램)
# 다른 방법
import matplotlib.pyplot as plt
import random

dice = []
for i in range(10):
    dice.append(random.randint(1,6))
plt.hist(dice, bins = 6)
plt.show

=============================================
# 다양한 그래프 그리기 (산점도)
import numpy as np
import matplotlib.pyplot as plt
x = np.random.randint(10,100,100)
y = np.random.randint(10,100,100)
size = np.random.rand(100) * 100

plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()

=============================================
# 다양한 그래프 그리기 (산점도)
# 다른방법
import matplotlib.pyplot as plt
import random

x = []
y = []
size = []

for i in range(200):
    x.append(random.randint(10,100))
    y.append(random.randint(10,100))
    size.append(random.randint(10,100))
    
plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()

=============================================
# ndarray : numpy 배열 / 특별한 배열 사용

=============================================
# numpy 학습 문자와 숫자
import numpy as np

a = np.array([1,2,3,4])

print(a)

=============================================
# numpy 학습 문자와 숫자
import numpy as np

a = np.array([1,2,'3',4])

print(a)

=============================================
# 0으로 이루어진 크기가 10인 배열 생성
import numpy as np

a = np.zeros(10) # 0으로 이루어진 크기가 10인 배열 생성

print(a)

=============================================
# 1로 이루어진 크기가 10인 배열 생성
import numpy as np

a = np.ones(10) # 1로 이루어진 크기가 10인 배열 생성

print(a)

=============================================
# 4행 * 4열의 단위 배열 생성
import numpy as np

a = np.eye(4) # 4행 * 4열의 단위 배열 생성

print(a)

=============================================
# 배열 원하는 행에 숫자 넣기
import numpy as np

print(np.arange(3))
print(np.arange(3,7))
print(np.arange(3,7,2))

=============================================
# 배열 원하는 행에 숫자 및 실수 넣기

import numpy as np

a = np.arange(1,2,0.1) #1이상 2미만 구간에서 0.1간격으로 실수 생성
b = np.arange(1,2,11) # 1부터 2 까지 11개 구간으로 나눈 실수 생성
# 특정 간격에 해당하는 값을 생성하고 싶을 때 arange()
# 특정 개수의 구간으로 나눈 값을 생성하고 싶을 때는 linspace()
print(a)
print(b)

=============================================
# 한가운데 빼고 산점도
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(-100, 100, 1000)
y = np.random.randint(-100, 100, 1000)
size = np.random.randint(3) * 100

mask1 = abs(x) > 50
mask2 = abs(y) > 50
x = x[mask1+mask2]
y = y[mask1+mask2]

plt.scatter(x,y,s=size,c=x,cmap='jet',alpha=0.7)
plt.colorbar()
plt.show()

"""
# 궁금한 지역의 인구 구조와 가장 비슷한 곳의 인구 구조 시각화
import numpy as np
import csv
 
# 데이터를 읽어온다.
f = open('age.csv')
data = csv.reader(f)
next(data)
data = list(data)
 
# 궁금한 지역의 이름을 입력받는다.
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1
result_name = ''
result = 0
 
# 궁금한 지역의 인구 구조를 저장한다.
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype=int)/int(row[2])
 
# 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
for row in data :
    away = np.array(row[3:], dtype=int)/int(row[2])
    s = np.sum((home-away)**2)
    if s < mn and name not in row[0] :
        mn = s
        result_name = row[0]
        result = away
 
# 궁금한 지역의 인구 구조와 가장 비슷한 곳의 인구 구조를 시각화한다.
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.title(name+' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label=name)
plt.plot(result, label=result_name)
plt.legend()
plt.show()