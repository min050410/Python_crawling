from urllib.request import urlopen, Request
from fake_useragent import UserAgent
import json

# fake_useragent 모듈을 통한 User-Agent 정보 생성
useragent = UserAgent()
print(useragent.chrome)
print(useragent.ie)
print(useragent.safari)
print(useragent.random)

# 헤더 선언 및 referer, User-Agent 전송
headers = {
    'referer': 'https://finance.daum.net/domestic/sectors',
    'User-Agent': useragent.chrome
}

# 주식 데이터 요청 URL
url = 'https://finance.daum.net/api/sectors/?includedStockLimit=2&page=1&perPage=30&fieldName=changeRate&order=desc&market=KOSPI&change=RISE&includeStocks=true&pagination=true'

# 주식 데이터 요청
response = urlopen(Request(url, headers=headers)).read().decode('utf-8')

# 응답 데이터 str 타입을 json 포맷으로 변환 및 data 저장
rank_json = json.loads(response)['data']
# print(rank_json)

print(f"날짜 : {rank_json[0]['date']}, 마켓: {rank_json[0]['market']}")
for rank in rank_json:
    print(
        f"종목 : {rank['sectorName']}, 상승/하강: {rank['change']}, 등락율 : {round(rank['changeRate']*100, 3)}")
