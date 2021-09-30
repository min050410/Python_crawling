import requests
# import json

json_url = "https://www.pokemonkorea.co.kr/pokemon-unite/menu126?stype1=&stype2=&number=2315&mode=view"

json_string = requests.get(json_url).text

infos = json_string.select('h3-deco')


    


