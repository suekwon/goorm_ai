#%%
# # python-binance 라이브러리 임포트
from binance.client import Client
import requests
import pyupbit
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import seaborn as sns

sns.set(font="AppleGothic",
        rc={"axes.unicode_minus": False},
        style='darkgrid')


# Binance 클라이언트 생성 (API 키 없이 사용)
client = Client("", "", tld='us')

# 가상자산 티커 설정 (예: BTC/USDT)
binance_ticker = "BTCUSDT"
upbit_ticker = "KRW-BTC"

# 환율 조회 함수


def get_usd_to_krw_rate():
    # 환율 API에서 USD에서 KRW로의 환율 정보 가져오기
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    # 환율 정보 출력
    usd_to_krw_rate = data['rates']['KRW']
    return usd_to_krw_rate

# 최근 1년간 데이터 조회 함수


def get_historical_data(ticker, interval='1d', lookback='365 days'):
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=int(lookback.split()[0]))
    start_time_str = start_time.strftime('%Y-%m-%d')
    end_time_str = end_time.strftime('%Y-%m-%d')

    if ticker.startswith('KRW-'):
        df = pyupbit.get_ohlcv(ticker, interval=interval, count=365)
    else:
        klines = client.get_historical_klines(
            ticker, interval, start_time_str, end_time_str)
        df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume',
                          'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        df['close'] = df['close'].astype(float)

    return df

# 메인 함수


def main():
    # 환율 조회
    usd_to_krw_rate = get_usd_to_krw_rate()
    print(f"현재 1 USD는 {usd_to_krw_rate:,.2f} KRW입니다.")

    # print("###########: ", usd_to_krw_rate)
    # Binance에서 최근 1년간 비트코인 가격 조회
    binance_df = get_historical_data(binance_ticker)
    binance_df['close_krw'] = binance_df['close'] * usd_to_krw_rate

    # Upbit에서 최근 1년간 비트코인 가격 조회
    upbit_df = get_historical_data(upbit_ticker)

    # 그래프 그리기
    plt.figure(figsize=(14, 7))
    plt.plot(binance_df.index,
             binance_df['close_krw'], label='Binance (원화 환산)')
    plt.plot(upbit_df.index, upbit_df['close'], label='Upbit')
    plt.xlabel('Date')
    plt.ylabel('Price (KRW)')
    plt.title('Binance vs Upbit BTC Price Comparison (Last 1 Year)')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
