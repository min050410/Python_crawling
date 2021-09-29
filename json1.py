import requests
import json

json_url = "https://askdjango.github.io/lv2/data.json"

json_string = requests.get(json_url).text

data_list = json.loads(json_string)

print(data_list)
for data in data_list:
    print(data)


    
