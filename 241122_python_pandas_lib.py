# %%
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./서울특별시 공공자전거 이용정보(월별)_24.1-6.csv', encoding='cp949')
data = pd.re
# %%
data[data['대여일자'] == 202401].head(10)
data[data['대여일자'] == 202401].tail(10)
# %%

data['대여소번호'].unique()
data['대여소번호'].value_counts().sort_values()
# %%
data.describe().to_csv('./data_describe.csv', encoding='cp949')
# %%
data['성별'].value_counts()
# %%

data[data['이용건수'] < 10]['이용시간(분)'].mean()
# %%
data[data['이용건수'] >= 10]['이용시간(분)'].mean()

# %%
data['성별'].value_counts().plot(kind='bar')


# %%
plt.plot([1, 2, 3], [1, 2, 3])
# %%

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.title("x-y graph")
plt.xlabel("time")
plt.ylabel("age")
# %%

data[data['성별'] == 'F']['이용건수'].plot(kind='hist')


# %%
# %%
