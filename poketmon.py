import requests
from bs4 import BeautifulSoup
# import json

json_url = "https://www.pokemonkorea.co.kr/pokemon-unite/menu126?stype1=&stype2=&number=2315&mode=view"

json_string = requests.get(json_url).text

# string 파일을 beautifulSoup 를 이용하여서 html 파일로 변환
soup = BeautifulSoup(json_string, 'html.parser')

# tags = soup.find_all('p')

list = []

for tag in soup.find_all('p'):  # 찾은 p 태그 내에 모든 txt를 출력
    list.append(tag.text)

null = list.count("")

for i in range(null):  # ''인 값 remove
    list.remove('')

# print(list[:18])
list = list[:18]

j = 0
print("   <거북왕>")
for i in range(18):
    if len(list[i]) <= 8:
        j += 1
        print(f"{j}. {list[i]}")
    else:
        print(f"   {list[i]}")
