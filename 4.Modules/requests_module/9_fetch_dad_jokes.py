import requests

def fetch_joke(word: str) -> dict: 
    baseurl = "https://icanhazdadjoke.com/search"
    parameters = {'term': word, 'limit': '3'}
    headers = {'Accept': 'application/json'}

    response = requests.get(baseurl, params=parameters, headers=headers)
    print(response.url)
    data = response.json()  # parses JSON directly
    print(data)

fetch_joke('joke')
