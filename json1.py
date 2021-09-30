import requests
import json

json_url = "https://askdjango.github.io/lv2/data.json"

json_string = requests.get(json_url).text

data_list = json.loads(json_string)['s2']

print(data_list)
for data in data_list:
    print(f"데이터 네임 : {data['name']}, 주소 : {data['url']}")

#굿
    
