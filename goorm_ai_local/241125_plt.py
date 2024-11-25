# %%
import matplotlib.pyplot as plt
import pandas as pd


# %%
a = [2, 3, 4, 5, 6, 7]
a = ['토끼', '사자', '호랑이', '곰', '여우', '늑대']
type(a)
# %%

b = pd.Series(a)
b.name = '동물'
type(b)
print(b.name)
# %%
# 엑셀컬럼 두 줄 만듬(a, b)
a = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
b = pd.Series([5, 6, 7, 8], ['a', 'b', 'c', 'd'])
c = pd.Series(['토끼', '사자', '호랑이', '곰'], ['a', 'b', 'c', 'd'])
# %%
# 컬럼 a, b 두 개를 하나로 합침
d = pd.DataFrame([a, b])
print(c.transpose())
# %%

dt = pd.DataFrame({'X': a, 'Y': b, 'Z': c})
# %%
dt['Z']  # 세로로 데이터가 들어옴
dt['a':'a']  # 가로로 데이터가 들어옴
dt[:2]

# %%
print(dt.loc['b':'c', 'Z':'Z'])
print(dt.iloc[1:3, 2:3])

# %%
dt['X'].sort_values(ascending=False)
dt.plot(kind='bar')

# %%

# %%
dt.plot(kind='bar')
plt.show()

# %%
# 1. 계약종별 전력사용량 월별_20190614.xls 파일 읽기
power = pd.read_excel('계약종별 전력사용량 월별_20190614.xls')

# %%
# 2. ‘시구’. ‘고객호수’ 데이터 선택
house = power[['시구', '고객호수(호)']]

# %%
# 3. ‘시구’. ‘사용량’ 데이터 선택
use = power[['시구', '사용량(kWh)']]

# 시구, 하나씩 나오게 groupby
# %%
power.groupby('시구').mean().plot(kind='bar')


# %% 
# 한글깨짐 해결
import seaborn as sns

sns.set(font="AppleGothic",
        rc={"axes.unicode_minus": False},
        style='darkgrid')
# %%
