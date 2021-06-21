import pandas as pd

df = pd.read_csv('data_path')  ## csv 데이터 읽어오기


## 데이터 파악하기
df.head()  ## 윗쪽 데이터 파악
df.tail()  ## 마지막 쪽 데이터 파악
df.columns  ## 데이터 컬럼 파악
df.isnull.sum()  ## 각 컬럼별 결측치 갯수 확인
df.isnull.sum().sum()  ## 전체 컬럼의 결측치 갯수의 합 확인
df.describe()  ## 각 컬럼 별 평균값등 정보 출력
df.info() ## 각 컬럼별 null값과 데이터 타입등 정보 출력
df['col_name'].value_counts()  ## 지정한 컬럼을 구성하는 인자들별 갯수 출력


## 데이터 프로세싱
df['col_name'].fillna(df['col_name'].mean(), inplace= True)  ## 지정한 컬럼의 결측치를 지정한 컬럼의 평균값으로 채워줌
df['col_name'].fillna('kk', inplace=True) ## 지정한 컬럼을 지정한 이름으로 채워줌
df = df.drop(columns='col_name')  ## 지정한 컬럼을 삭제 후 다시대입
