import requests
import json

baseUrl="https://api.upcitemdb.com/prod/trial/lookup"
parameters={"upc":"012993441012"}  ###key value for particular product
response=requests.get(baseUrl,params=parameters)
print(response.url)

content=json.loads(response.content)  ##json.loads used to convert json to dict format
print(content)

item=content['items']
item_info=item[0]

keys=item_info.keys()  ##extrat keys from dict
print(keys)

title=item_info['title']  ## extracting the title from the items_info
brand=item_info['brand']

print(title)
print(brand)