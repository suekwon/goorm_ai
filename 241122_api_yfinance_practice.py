# %%
import requests
import yfinance as yf
import time

# %%


def get_gold_price():
    # 티커 심볼'GC=F'는 금 선물 가격을 의미합니다.
    gold = yf.Ticker("GC=F")
    gold_data = gold.history(period="1d")
    current_price = gold_data['Close'].iloc[-1]
    return current_price

# 가장 최근 종가 가격


def track_gold_price(interval=1):
    while True:
        price = get_gold_price()
        print(f"현재 금 가격: ${price}")
        time.sleep(interval)  # 주어진 시간(초)마다 업데이트

# 예제: 1시간(3600초)마다 금 가격 추적
# track_gold_price(interval=0.5)


# %%

def exch_caluculator(from_curr, to_curr, amount):

    url = f"https://open.er-api.com/v6/latest/{from_curr}"
    response = requests.get(url)
    print(response)

    data = response.json()
    # print(data)
    # print(data['rates']['KRW']
    exch_data = data['rates'][to_curr]

    # 환율 계산기
    # 입력: 외국통화(USD), 필요외국통화금액, 환율국가(KRW)
    # 출력: 환율*필요외국통화금액

    # amount = 100
    result = amount * exch_data
    print(exch_data)
    return result


# 계속 반복, 사용자가 그만한다고 할 때까지
print("환율 계산기")
print("="*20)
while True:
    price = float(input("변환 금액을 입력하세요: "))
    curr1 = input("변환하고 싶은 통화를 입력하세요: ")
    curr2 = input("어떤 통화를 바꾸고 싶으신지 입력하세요: ")
    converted = exch_caluculator(curr1, curr2, price)

    print(f"{price} {curr1} 은 {converted} {curr2}입니다.")
    cont = input("계속 진행할까요? (Y/N): ").upper()
    if cont == 'N':
        break
