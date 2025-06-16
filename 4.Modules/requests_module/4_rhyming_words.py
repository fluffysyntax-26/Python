import requests

# a program which will give three rhyming words

def get_rhymes(word): 
    baseurl = "https://api.datamuse.com/words"
    param_dict = {}
    param_dict['rel_rhy'] = word
    param_dict['max'] = '3'
    response = requests.get(baseurl, params = param_dict)
    words = response.json()

    print(words)
    rhymes = [d['word'] for d in words]
    return rhymes

print(get_rhymes("map"), "\n")
print(get_rhymes('funny'))