#8월 일별 기온 데이터를 상자 그림으로 표현하기
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