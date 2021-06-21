import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


## 데이터의 관계 분석하는 corr그래프 그리기
sns.heatmap(df.corr(), annot=True, linewidths=0.3 )  ## 그릴 데이터, 수치로 데이터비율 나타내기, 히트맵 격자 사이 거리 설정
plt.gcf().set_size_inches(14,10)                     ## 그래프의 크기 설정


## 원그래프 = 한 컬럼안에 존재하는 데이터 비율로 원 그래프 그리기
f, ax = plt.subplots(1,2,figsize=(18,8))                   ## 그래프를 그릴 그림판 크기 설정
df['col_name'].value_counts().plot.pie(explode = [0,0.1], autopct = '%.2f', ax=ax[0], shadow = True) ## 그래프의 그림자나 수치 표현등의 설정


## 막대 카운트 그래프 =  한 컬럼안에 존재하는 데이터 카운팅 막대 그래프 그리기
sns.set_style('whitegrid')                 ## 그래프 배경 스타일 설정
sns.countplot('col_name', data = df, ax = ax[1])  ## 지정한 컬럼의 인자값의 카운트 결과를 막대 카운트 그래프로 출력


## 막대 카운트 그래프 = 지정한 컬럼 안의 존재하는 데이터 종류로 나눈 뒤 그 종류 별 hue값으로 나눈 카운팅 그래프 그리기
sns.countplot('col_name', hue = '???', data=df, ax = ax[1])
plt.show()


## 퍼센트 바 그래프 = 지정한 컬럼의 인자를 나누고 그 인자들중 y로 지정한 컬럼에 해당하는 퍼센테이지를 바 그래프로 나타냄
sns.barplot(x = 'col_name', y = '???', data = df, ax = ax[0])