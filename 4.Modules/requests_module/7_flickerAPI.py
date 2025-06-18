import requests
import webbrowser

# paste the api key here by signing up on flickr
flickr_key = "yourkeyhere"

def fetch_data(tags_string): 
    baseurl = "https://api.flickr.com/services/rest/"

    # parameters for the url
    param_dict = {}
    param_dict['api_key'] = flickr_key # from the global var
    param_dict['tags'] = tags_string # function parameter, must be a comman separated value
    param_dict['tag_mode'] = 'all'
    param_dict['method'] = 'flickr.photos.search'
    param_dict['per_page'] = 5
    param_dict['media'] = 'photos'
    param_dict['format'] = 'json'
    param_dict['nojsoncallback'] = 1

    # response from the api 
    flickr_response = requests.get(baseurl, param_dict)
    
    # print url
    print(flickr_response.url)

    return flickr_response.json()

result = fetch_data('river, mountains')

photos = result['photos']['photo']
for photo in photos: 
    owner = photos['owner']
    photo_id = photo['id']
    url = f'https://www.flickr.com/photos/{owner}/{photo_id}'
    webbrowser.open(url)


