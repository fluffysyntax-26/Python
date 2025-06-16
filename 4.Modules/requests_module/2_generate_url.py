# specifying the key:value pair and generating the url automatically
import requests
import json

key_val = {'ml':'ringing in the ears'}
page = requests.get("https://api.datamuse.com/words", params = key_val)
print(page.text[:])
print(page.url)

# convert the request object into json
json_content = page.json() 
data = json.dumps(json_content, indent=2)
print(data)