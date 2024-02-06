"""
# 인구 구조 알고싶은 동 검색

import csv

f=open('korea_age.csv')
data = csv.reader(f)
result = []
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')

for row in data:
    if name in row[0]:
        for i in row[3:]:
            result.append(int(i.replace(',','')))
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', family = 'Malgun Gothic')
plt.title(name + '지역의 인구 구조')
plt.plot(result)
plt.show()

================================================================================

# 막대, 수평 막대그래프 그리기
import csv

f=open('korea_age.csv')
data = csv.reader(f)

result = []
for row in data:
    if '신도림' in row[0]:
        for i in row[3:]:
            result.append(int(i))
import matplotlib.pyplot as plt
plt.bar(range(101), result) # plt.barh(range(101), result)로 바꾸면 수평 막대 그래프로 표현
plt.show()

"""

# 동네 인구 구조를 항아리 모양 그래프로 그리기

import csv

f=open('gender.csv')
data = csv.reader(f)

m=[]
f=[]
name = input('찾고 싶은 지역의 이름을 알려주세요 : ')

for row in data:
    if name in row[0]:
        for i in row[3:104]:
            m.append(-int(i))
        for i in row[106:] :
            f.append(int(i))
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title(name + '지역의 남녀 성별 인구 분포')
plt.barh(range(101),m, label='남성')
plt.barh(range(101),f, label='여성')
plt.legend()
plt.show()
