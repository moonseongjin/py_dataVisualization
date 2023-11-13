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