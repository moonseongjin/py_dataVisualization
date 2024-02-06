"""
# 유임 승차 비율이 가장 높은 역 찾기

import csv

f = open('subwayfee(3).csv')
data = csv.reader(f)
next(data)

mx = 0
rate = 0
mx_station = ''

for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
#유무임 승차 인원을 합해서 100,000명 이상인 경우만
    if row[6] != 0 and (row[4] + row[6]) > 100000: 
        rate = row[4] / (row[4] + row[6])
        if rate > mx:
            mx = rate 
            mx_station = row[3] + ' ' + row[1] # row[3] = 역이름, row[1] = 몇 호선
print(mx_station, round(mx*100,2))

==================================================================================

import csv
f = open('subwayfee(3).csv')
data = csv.reader(f)

next(data)
mx = [0] * 4
mx_station = [''] * 4
label = ['유임승차', '유임하차', '무임승차', '무임하차']

for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
        if row[i] > mx[i-4]:
            mx[i-4] = row[i]
            mx_station[i-4] = row[3] + ' ' + row[1]
        
for i in range(4):
    print(label[i]+ ' 가장 많은 역과 인원수 : ' + mx_station[i], mx[i])

==================================================================================
import csv
import matplotlib.pyplot as plt

f = open('subwayfee(3).csv')
data = csv.reader(f)

next(data)
mx = [0] * 4
mx_station = [''] * 4
label = ['유임승차', '유임하차', '무임승차', '무임하차']
c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']
plt.rc('font', family = 'Malgun Gothic')

subway = input('어떤 역이 궁금하신가요? ')

for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    if subway in row[3]:
        plt.figure(dpi=300)
        plt.title(row[3] + ' ' + row[1])
        plt.pie(row[4:8], labels = label, colors = c, autopct = '%.1f%%')
        plt.axis('equal')
        plt.savefig(row[3] + ' ' + row[1] + '.png')
        plt.show()

"""

# 모든 역의 유무임 승하차 비율을 파이 차트로 나타내기
import csv
import matplotlib.pyplot as plt

f = open('subwayfee(3).csv')
data = csv.reader(f)

next(data)
mx = [0] * 4
mx_station = [''] * 4
label = ['유임승차', '유임하차', '무임승차', '무임하차']
c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']
plt.rc('font', family = 'Malgun Gothic')



for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    
        plt.figure(dpi=300)
        plt.title(row[3] + ' ' + row[1])
        plt.pie(row[4:8], labels = label, colors = c, autopct = '%.1f%%')
        plt.axis('equal')
        plt.savefig(row[3] + ' ' + row[1] + '.png')
        plt.show()