from requests import get
from configuration import get_config

# ACCESS_TOKEN = get_config('access_token')
API_KEY = get_config('api_key')
BASE_URL = get_config('base_url')
# header = {'Authorization': 'Bearer ' + ACCESS_TOKEN}


# https://api.themoviedb.org/3/search/movie?api_key=3386c5875b2a009399b57b928eb7b2e5&language=en-US&query=matrix&page=1&include_adult=false

def test_existing_movie():
    tested_movie = 'matrix'
    full_request_url = '{}/search/movie?api_key={}&query={}'.format(BASE_URL, API_KEY,tested_movie)
    response = get(url=full_request_url)
    movie_title = response.json()['results'][0]['title'].lower()
    assert tested_movie in movie_title


def test_non_existing_movie():
    tested_movie = 'the pavel'
    full_request_url = '{}/search/movie?api_key={}&query={}'.format(BASE_URL, API_KEY, tested_movie)
    response = get(url=full_request_url)
    try:
        movie_title = response.json()['results'][0]['title'].lower()
        assert tested_movie in movie_title
    except:
        assert 1==0
