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