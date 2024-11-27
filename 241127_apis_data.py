# %%

import os
import requests
from dotenv import load_dotenv
import pandas as pd
import xml.etree.ElementTree as ET

# %%

import requests
import xml.etree.ElementTree as ET
import pandas as pd


def get_stock_price(service_key, num_of_rows=10, page_no=1):
    # API 엔드포인트 URL
    base_url = "https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"

    # 파라미터 설정
    params = {
        'serviceKey': service_key,
        'numOfRows': num_of_rows,
        'pageNo': page_no
    }

    try:
        # API 호출
        response = requests.get(base_url, params=params, verify=False)
        response.raise_for_status()

        # XML 파싱
        root = ET.fromstring(response.content)

        # 데이터 추출
        items = []
        for item in root.findall('.//item'):
            stock_data = {}
            for child in item:
                stock_data[child.tag] = child.text
            items.append(stock_data)

        # DataFrame 생성
        df = pd.DataFrame(items)

        # 컬럼명 한글로 변경
        column_names = {
            'basDt': '기준일자',
            'srtnCd': '종목코드',
            'itmsNm': '종목명',
            'mrktCtg': '시장구분',
            'clpr': '종가',
            'vs': '전일대비',
            'fltRt': '등락률',
            'mkp': '시가',
            'hipr': '고가',
            'lopr': '저가',
            'trqu': '거래량',
            'trPrc': '거래대금',
            'lstgStCnt': '상장주식수',
            'mrktTotAmt': '시가총액'
        }
        df = df.rename(columns=column_names)

        return df

    except requests.exceptions.RequestException as e:
        print(f"API 호출 중 오류 발생: {e}")
        return None


# %%
service_key = os.getenv("STOCK_API_SERVICE_KEY")
print(service_key)

# API 엔드포인트 URL
base_url = "https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"

# 파라미터 설정
params = {
    'serviceKey': service_key,
    'numOfRows': 10,
    'pageNo': 1,
    'itmsNm': '삼성전자'
}
res = requests.get(base_url, params=params)
res.text
# %%
# 인증키를 입력하세요
service_key = os.getenv("STOCK_API_SERVICE_KEY")

# API 호출
stock_df = get_stock_price(service_key, num_of_rows=5)

# 결과 출력
if stock_df is not None:
    print(stock_df)
# %%


# %%
'https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo?serviceKey=wLG27wHT5cdba3w3E%2Bjl05k%2F6s4%2Bl7iqBuXzVU%2BD9P%2BeXcZsDcIZufilv8yeojkJv%2BHevNEsVG9SZsQsvMzF9Q%3D%3D&numOfRows=1&pageNo=1&resultType=xml&basDt=20241126&itmsNm=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90'

# %%
base_url
# %%
service_key
# %%
ss = base_url + "?serviceKey=" + service_key + "&numOfRows=5" + "&pageNo=1"
# %%
requests.get(ss)
# %%
