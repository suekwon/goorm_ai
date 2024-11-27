#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pykrx import stock
from datetime import datetime, timedelta

# %%
# 어제 날짜 구하기
yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y%m%d")

df = stock.get_market_cap(yesterday)
df = df.sort_values(by='거래대금', ascending=False)
top_5 = df.head(5)

top_5.index = [stock.get_market_ticker_name(ticker) for ticker in top_5.index]

# 거래대금에 콤마 추가
top_5['거래대금'] = top_5['거래대금'].apply(lambda x: format(x, ','))

print(top_5[['거래대금']])
# %%

# %%

# 어제 날짜 구하기
yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y%m%d")

# 거래량 데이터 가져오기 [[1](https://github.com/sharebook-kr/pykrx)]
df = stock.get_market_ohlcv(yesterday)
df = df.sort_values(by='거래량', ascending=False)
top_5 = df.head(5)

# 티커를 종목명으로 변환
top_5.index = [stock.get_market_ticker_name(ticker) for ticker in top_5.index]

# 거래량에 콤마 추가
top_5['거래량'] = top_5['거래량'].apply(lambda x: format(x, ','))

print(top_5[['거래량']])

# %%


def get_top_volume_stocks(date):
    # 거래량 데이터 가져오기
    df = stock.get_market_ohlcv(date)
    df = df.sort_values(by='거래량', ascending=False)
    top_5 = df.head(5)

    # 티커를 종목명으로 변환
    top_5.index = [stock.get_market_ticker_name(ticker) for ticker in top_5.index]

    # 거래량에 콤마 추가
    top_5['거래량'] = top_5['거래량'].apply(lambda x: format(x, ','))

    return print(top_5[['거래량']])

# 날짜 입력 예시 (YYYYMMDD 형식)
date = "20241126"
get_top_volume_stocks(date)
# %%

import time

def get_top_volume_stocks(now):

    # 거래량 데이터 가져오기
    df = stock.get_market_ohlcv(now)
    df = df.sort_values(by='거래량', ascending=False)
    top_5 = df.head(5)
    
    # 티커를 종목명으로 변환
    top_5.index = [stock.get_market_ticker_name(ticker) for ticker in top_5.index]
    
    # 거래량에 콤마 추가
    top_5['거래량'] = top_5['거래량'].apply(lambda x: format(x, ','))
    
    print("\n현재시간:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(top_5[['거래량']])

while True:    
    # 현재 날짜 가져오기
    now = datetime.now().strftime("%Y%m%d")
    get_top_volume_stocks(now)
    
    user_input = input("프로그램을 종료하려면 'q'를 입력하세요 (10초 대기): ")
    if user_input.lower() == 'q':
        print("프로그램을 종료합니다.")
        break    
    time.sleep(0.1)  # 1분 대기
# %%

# 3. 
# 특정 기업 주가를 조회
# 주가를 활용 매매전략을 소개, 추천,
# 대표적인 매매전략 하나를 파이썬 코드로 작성

#%%
now = datetime.now().strftime("%Y%m%d")
df = stock.get_market_ohlcv(now)
df.columns




#%%
#%%
# pip install pykiwoom
# pip install PyQt5==5.13
# from pykiwoom.kiwoom import *


# %%
