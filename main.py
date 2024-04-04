import requests
import json
from pprint import pprint 
import pandas as pd

api_url = "https://gateway.apiportal.ns.nl/nsapp-stations/v2"
headers =  {"Cache-Control": "no-cache","Ocp-Apim-Subscription-Key": ""}
#todo = {"userId": 1, "title": "Buy milk", "completed": False}
#response = requests.get(api_url)
response = requests.get(api_url, headers=headers)
data = response.json()
payload = data['payload']
#pprint(data['payload'])


for line in payload:
    print(type(line))
    print(line)

print(type(payload))

df = pd.DataFrame(payload).explode('namen', 'synoniemen')

print(df.head)

df.to_csv("file_name2.csv", encoding='utf-8', index=False)
