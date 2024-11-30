# %%
from matplotlib import font_manager, rc
import mplfinance as mpf
import matplotlib.font_manager as fm
import seaborn as sns
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

sns.set(font="AppleGothic",
        rc={"axes.unicode_minus": False},
        style='darkgrid')
# %%


# # 파이썬으로 ...만들기
# # 1. 기능정의 (가상자산 가격을 조회하는 기능)
# # -LLM: 가상자산이 무엇인지 간단하게 설명해줘.
# #     : 어떤 종류가 있는지 알려줘.
# #    :  대한민국에서 거래할 수 있는 가상자산이 무엇인지와, 어디서 거래할 수 있는지 알려줘.

# # 2. 기능을 어떻게 구현할지 (파이썬, LLM: mistral) -> LLM 도움으로 코드 작성하기
# # : upbit 거래소에서 가상자산(..종류)의 가격을 조회하는 기능을 파이썬으로 만들어보자 (pyupbit 라이브러리를 사용해줘.)
# # : 단계별로 차근차근히 실행할 수 있게 알려줘.
# # (비트코인 원화가격 조회하기)
# # 3. 구현을 실제로 해보기
# # : 코드 설명

# # %%

# import matplotlib.font_manager as fm
# import matplotlib.pyplot as plt
# from IPython.core.interactiveshell import InteractiveShell
# import pandas as pd

# import mplfinance as mpf

# daily = pd.read_csv('./SP500_NOV2019_Hist.csv', index_col=0, parse_dates=True)
# daily.index.name = 'Date'
# daily.shape
# daily.head(3)
# # mpf.plot(daily)

# # %matplotlib inline
# # Update this path to the location of your Korean font
# font_path = '/Users/cactus/Library/Fonts/NanumSquareR.ttf'
# fontprop = fm.FontProperties(fname=font_path, size=10)
# plt.rc('font', family=fontprop.get_name())

# # plt.rcParams['font.sans-serif'] = ['simHei', 'Malgun Gothic']
# # plt.rcParams['axes.unicode_minus'] = False
# # %%
# InteractiveShell.ast_node_interactivity = "all"
# df = pd.read_csv('./SPY_20110701_20120630_Bollinger.csv',
#                  index_col=0, parse_dates=True)


# # %%
# apd = mpf.make_addplot(df['LowerB'], type='scatter',
#                        label="추가된 scatter", title="한글폰트"
#                        )

# mpf.plot(df, addplot=apd)

# #%%
