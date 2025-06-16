import requests

d = {'q': 'violins and guitars', 'tbm' : "isch"} # isch stands for image search
results = requests.get('https://google.com/search', params = d)
print(results.url, '\n')
print(results.text)