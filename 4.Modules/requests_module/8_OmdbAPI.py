# fetch movie info from omdb

import requests

def get_movie_info(name: str) -> dict:
    url = " http://www.omdbapi.com/?&apikey=53f1c48d"

    #format movie name
    movie_name = "+".join(name.split())
    params_dict = {'t' : movie_name, 'r':'json'}
    request = requests.get(url, params=params_dict)
    data = request.json()

    return data

def get_RT_ratings(movie_info: dict) -> int:
    '''
    Fetches the Rotten Tomato Ratings from the movie_info dict, returns an int as rating
    if rating does not exist returns -1     
    '''
    rating = -1
    for ratings in movie_info["Ratings"]: 
        if ratings['Source'] == "Rotten Tomatoes": 
            rating = int(ratings["Value"][:-1])

    # convert this into an int
    return rating

def print_movie_info(movie_info): 
    for info, val in movie_info.items(): 
        print(f"{info}:{val}")


movie_info = get_movie_info("back to the future")
print(get_RT_ratings(movie_info))



