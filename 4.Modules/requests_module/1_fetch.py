# fetching a page using the datamuse api 

import requests 
import json

page = requests.get("https://api.datamuse.com/words?rel_jjb=ocean")
print(type(page))

words = page.text[:] # load all data into a string
print(page.url) # prints the url from which the data was fetched from 

# converting the data into readable format using the json module
x = page.json() # turn page.text into a python object
print(type(x))

# print the list items (using a for loop) 
for item in x: 
    print(item)

# print the data in json-like format
print(json.dumps(x, indent=2))
