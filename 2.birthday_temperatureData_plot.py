"""
# 기본 그래프 그리기
matplotlib 라이브러리 :

파이썬에서 2D 형태의 그래프, 이미지 등을 그릴 때 주로사용
========================================================
# 대각선
import matplotlib.pyplot as plt
plt.plot([10,20,30,40])
plt.show()
========================================================
# 대각선 꺾기
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[12,43,25,15])
plt.show()
========================================================
# 범례 집어넣기
import matplotlib.pyplot as plt
plt.title('legend')
plt.plot([10,20,30,40],label='asc') # asc = 증가 
plt.plot([40,30,20,10],label='desc') # desc = 감소
plt.legend()
plt.show()
========================================================
# 그래프 색상 바꾸기
import matplotlib.pyplot as plt
plt.title('color') # 제목설정
========================================================
# 그래프 그리기
plt.plot([10,20,30,40], color = 'skyblue', label='skyblue')
plt.plot([40,30,20,10], 'pink', label='pink') 
plt.legend() # 범례표시
plt.show()
========================================================
# 그래프 선 모양 바꾸기
import matplotlib.pyplot as plt
plt.title('linestyle') # 제목설정
========================================================
# 그래프 그리기
plt.plot([10,20,30,40],'r', linestyle='--', label = 'dashed') 
plt.plot([40,30,20,10],'g', ls=':', label= 'dotted') 
plt.legend() # 범례표시
plt.show()
========================================================
# 마커 모양 바꾸기
import matplotlib.pyplot as plt
plt.title('marker') # 제목설정
========================================================
# 그래프 그리기
plt.plot([10,20,30,40],'r.', label = 'circle') #r.은 레드 점모양
plt.plot([40,30,20,10],'g^', label= 'triangle up') #g^는 그린 삼각형
plt.legend() # 범례표시
plt.show()
"""

"""
# 매년 2월 14일 최고 기온 데이터 시각화
import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data) #헤더 건너띄기
result = [] #최고 기온 데이터를 저장할 리스트 생성

for row in data:
    if row[-1] != '' : # row[-1] 기온 위치를 나타냄 # 최고 기온 데이터 값이 존재한다면 
        if row[0].split('-')[1] == '02' and row[0].split('-')[2] =='14':
            result.append(float(row[-1])) # result 리스트에 최고 기온 값 추가
plt.plot(result,'r') # result 리스트에 저장된 값을 빨간색 그래프로 그리기
plt.show() # 그래프로 나타내기
======================================================================================
# 매년 2월 14일 최고, 최저 기온
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data) #헤더 건너띄기
high = [] #최고 기온 데이터를 저장할 리스트 생성
low = [] #최저 기온 데이터를 저장할 리스트 생성

for row in data:
    if row[-1] != '' and row[-2] !='' : # 최고 기온 값과 최저 기온 값이 존재한다면
        if 1983 <= int(row[0].split('-')[0]): # 1983년 이후 데이터라면
            if row[0].split('-')[1] == '02' and row[0].split('-')[2] =='14':
                high.append(float(row[-1]))
                low.append(float(row[-2]))
plt.plot(high,'hotpink') 
plt.plot(low,'skyblue')
plt.show() # 그래프로 나타내기
"""

# 내 생일의 기온 변화를 그래프로 그리기

import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data) 
high = [] 
low = []

for row in data:
    if row[-1] != '' and row[-2] !='' : 
        if 1996 <= int(row[0].split('-')[0]): 
            if row[0].split('-')[1] == '06' and row[0].split('-')[2] =='13':
                high.append(float(row[-1]))
                low.append(float(row[-2]))
plt.rc('font', family='Malgun Gothic') # 맑은 고딕 기본 글꼴로 설정
plt.rcParams['axes.unicode_minus'] =False # 마이너스 기호 깨짐 방지
plt.title('내 생일의 기온 변화 그래프') # 제목 설정

plt.plot(high,'hotpink', label='high') 
plt.plot(low,'skyblue', label='low')
plt.legend() # 범례표시
plt.show() #그래프로 나타내기