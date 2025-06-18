import requests
import json

params_dict = {'entity':'musicTrack', 'term':'lana del ray'}
request = requests.get('https://itunes.apple.com/search?', params = params_dict)
data = request.json()

print(type(data))
with open("lana_songs.json", 'w') as json_file:
    json.dump(data, json_file, indent = 2)

for song in data['results']: 
    print(song['trackName'])