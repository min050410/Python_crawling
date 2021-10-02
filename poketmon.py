import requests
from bs4 import BeautifulSoup
# import json

json_url = "https://www.pokemonkorea.co.kr/pokemon-unite/menu126?stype1=&stype2=&number=2315&mode=view"

json_string = requests.get(json_url).text

# string 파일을 beautifulSoup 를 이용하여서 html 파일로 변환
soup = BeautifulSoup(json_string, 'html.parser')

# tags = soup.find_all('p')

for tag in soup.find_all('p'):
    print(tag.text)  # 찾은 p 태그 내에 모든 txt를 출력


