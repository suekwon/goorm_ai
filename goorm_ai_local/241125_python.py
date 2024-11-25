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

# # %%

# #%%


# %%

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import mplfinance as mpf
import pandas as pd

# Set the font properties
# Update this path to the location of your Korean font
font_path = '/Users/cactus/Library/Fonts/NanumSquareR.ttf'
fontprop = fm.FontProperties(fname=font_path, size=10)
plt.rc('font', family=fontprop.get_name())

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# Your existing code
df = pd.read_csv('./SPY_20110701_20120630_Bollinger.csv',
                 index_col=0, parse_dates=True)
mpf.make_addplot(df['LowerB'], type='scatter',
                 label="추가된 scatter", title="한글폰트")

# Plotting code
apd = mpf.make_addplot(df['LowerB'], type='scatter',
                       label="추가된 scatter", title="한글폰트"
                       )
mpf.plot(df, addplot=apd, title="한글폰트가 적용된 차트")
# plt.show()

# %%
