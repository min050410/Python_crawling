import json
from urllib.request import urlopen, Request
from fake_useragent import UserAgent

useragent = UserAgent()

headers = {
    'referer': 'https://search.naver.com/search.naver?where=nexearch&sm=tab_bck&ie=utf8&ug_cid=mwk&query=%EC%83%9D%EB%85%84%EC%9B%94%EC%9D%BC%20%EC%9A%B4%EC%84%B8',
    'User-Agent': useragent.chrome

}

url = "https://m.search.naver.com/p/csearch/dcontent/external_api/json_todayunse_v2.naver?_callback=window.__jindo2_callback._fortune_my_0&gender=m&birth=20050410&solarCal=solar&time="

response = urlopen(Request(url, headers=headers))  # .read().decode("utf-8")



# ['result'][0]


# print(luck_json)
