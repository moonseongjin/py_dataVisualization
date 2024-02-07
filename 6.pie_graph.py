"""
# 기본 파이

import matplotlib.pyplot as plt

size = [2441,2312,1031,1233]
plt.axis('equal')
plt.pie(size)
plt.show()
==============================================
# 레이블 추가 파이

import matplotlib.pyplot as plt

plt.rc('font', family = 'Malgun Gothic')
size = [2441,2312,1031,1233]
label = ['A형','B형','AB형','O형']
plt.axis('equal')
plt.pie(size, labels=label)
plt.show()
================================================================================
# 비율 및 범례 표시

import matplotlib.pyplot as plt

plt.rc('font', family = 'Malgun Gothic')
size = [2441,2312,1031,1233]
label = ['A형','B형','AB형','O형']
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%') # 소수점 아래 둘째 자리에서 반올림
plt.legend()
plt.show()

================================================================================
# 색 및 돌출 효과 정하기

import matplotlib.pyplot as plt

plt.rc('font', family = 'Malgun Gothic')
size = [2441,2312,1031,1233]
label = ['A형','B형','AB형','O형']
color = ['darkmagenta','deeppink','hotpink','pink']
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%', colors=color, explode=(0,0,0.1,0)) 
plt.legend()
plt.show()

"""
# 제주특별자치도 지역의 남녀 성별 비율 파이 모양으로 그리기
import csv

f=open('gender.csv')
data = csv.reader(f)

size = []
name = input('찾고 싶은 지역의 이름을 알려주세요 : ') # 지역이름 받기

for row in data:
    if name in row[0]:
        m=0 # 남성 인구수를 누적해서 더할 변수 초기화하기
        f=0 # 여성 인구수를 누적해서 더할 변수 초기화하기
        for i in range(101):
            m += int(row[i+3].replace(',','')) # 남성 인구수를 누적해서 더하기
            f += int(row[i+106].replace(',','')) # 여성 인구수를 누적해서 더하기
        break
size.append(m)
size.append(f)
print(size)

import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
color = ['crimson', 'darkcyan'] # 색상 설정
plt.axis('equal')
plt.title(name+' 지역의 남녀 성별 비율') 
plt.pie(size, labels = ['남', '여'], autopct='%.1f%%', colors=color,startangle=90)

plt.show()
