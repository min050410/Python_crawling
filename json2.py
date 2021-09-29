from urllib.request import urlopen, request
from fake_useragent import Useragent
import json

#user-agent 정보 생성
useragent = Useragent()
print(useragent.chrome)
print(useragent.ie)
print(useragent.safari)
print(useragent.random)

#헤더 선언 및 re    