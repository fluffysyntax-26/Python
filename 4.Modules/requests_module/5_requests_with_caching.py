import requests_with_caching
import json

request = requests_with_caching.get("https://www.datamuse.com/api/words?rel_jja=yellow", permanent_cache_file='datamuse_api_cache.txt')
print(request.text[:100])

# bugs in the requests_with_caching module