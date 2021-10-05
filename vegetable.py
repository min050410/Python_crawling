import requests
from bs4 import BeautifulSoup


json_url = "http://apis.data.go.kr/6260000/EgMarketCost/getDailyCost?serviceKey=Yf8CKY2ztyZit92xmxsHJJLZr%2B47fcT4dDiZyhelKmqkjcATuJ4oCLfUWDeNHJuMA%2BNvXz9UhBTyV%2B8ZQdT8WQ%3D%3D&numOfRows=5&pageNo=1"

json_string = requests.get(json_url).text


soup = BeautifulSoup(json_string, 'html.parser')

print(soup)
