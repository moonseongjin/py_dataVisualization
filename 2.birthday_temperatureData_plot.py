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