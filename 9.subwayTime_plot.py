"""
# 출근 시간대 사람들이 가장 많이 타고 내리는 역은 어디일까?

import csv
f= open('subwaytime.csv')
data=csv.reader(f)
next(data)
next(data)

result = []

for row in data:
    row[4:] = map(int, row[4:])
    result.append(row[10]) # 아침 7시 승차 데이터

import matplotlib.pyplot as plt
result.sort() # 오름차순 정렬
plt.bar(range(len(result)), result)
plt.show()

=================================================================
# 출근 시간대 사람들이 가장 많이 타고 내리는 역 찾기

import csv
f= open('subwaytime.csv')
data=csv.reader(f)
next(data)
next(data)

mx = 0
mx_station = ''

for row in data:
    row[4:] = map(int, row[4:])
    a = row[11:16:2] # 하차 인원 값 추출하기
    if sum(a) > mx :
        mx = sum(a)
        mx_station = row[3] + '('+row[1]+')'
print(mx_station, mx)

=================================================================
# 특정 시간에 사람들이 가장 많이 타고 내리는 역 찾기

import csv
f= open('subwaytime.csv')
data=csv.reader(f)
next(data)
next(data)

mx = 0
mx_station = ''
t = int(input('몇 시의 승차 인원이 가장 많은 역이 궁금하세요? : '))


for row in data:
    row[4:] = map(int, row[4:])
    a = row[4+(t-4)*2] # 입력 받은 시각의 승차 인원 값 추출하기
    if a > mx: # 모든 데이터 탐색
        mx = a
        mx_station = row[3] + '('+row[1]+')'
print(mx_station, mx)

=================================================================
# 시간대별로 사람들이 가장 많이 타고 내리는 역은 어디일까?
# i = j * 2 + 4 
import csv
f= open('subwaytime.csv')
data=csv.reader(f)
next(data)
next(data)

t = 24
mx = [0] * t # 시간대별 최대 승차 인원 저장 리스트 초기화
mx_station = [''] * t # 시간대별 최대 승차 인원 역 이름 저장 리스트 초기화


for row in data:
    row[4:] = map(int, row[4:])
    for j in range(t):
        a = row[j*2+4]
        if a > mx[j]:
            mx[j] = a 
            mx_station[j] = row[3]+'('+str(j+4)+ '시)'


import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
plt.bar(range(t),mx)
plt.xticks(range(t), mx_station,rotation = 90)        
plt.show()

=================================================================
# 시간대별로 하차 인원이 가장 많은 역을 찾는 코드

import csv
f= open('subwaytime.csv')
data=csv.reader(f)
next(data)
next(data)

t = 24
mx = [0] * t # 시간대별 최대 승차 인원 저장 리스트 초기화
mx_station = [''] * t # 시간대별 최대 승차 인원 역 이름 저장 리스트 초기화


for row in data:
    row[4:] = map(int, row[4:])
    for j in range(t):
        b = row[5+j*2]
        if b > mx[j]:
            mx[j] = b 
            mx_station[j] = row[3]+'('+str(j+4)+ '시)'


import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
plt.bar(range(t),mx, color='b')
plt.xticks(range(t), mx_station,rotation = 90)        
plt.show()

"""

# 지하철 시간대별 승하차 인원 추이를 나타내는 코드

import csv
import matplotlib.pyplot as plt

f= open('subwaytime.csv')
data=csv.reader(f)
next(data)
next(data)

t = 24
s_in = [0] * t
s_out = [0] * t

for row in data:
    row[4:] = map(int, row[4:])
    for i in range(t):
        s_in[i] += row[4+i*2]
        s_out[i] += row[5+i*2]
        
plt.rc('font', family = 'Malgun Gothic')
plt.title('지하철 시간대별 승하차 인원 추이')
plt.plot(s_in, label='승차')
plt.plot(s_out, label='하차')
plt.legend()
plt.xticks(range(t), range(4,28))        
plt.show()