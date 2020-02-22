# encoding: UTF-8
from requests import get
from configuration import get_config

API_KEY = get_config('api_key')
BASE_URL = get_config('base_url')
EXISTING_MOVIE = 'matrix'
NON_EXISTING_MOVIE = 'pavelzagalsky'
SEARCH_MOVIE_QUERY = '{}/search/movie?api_key={}'.format(BASE_URL, API_KEY)


# https://api.themoviedb.org/3/movie/603?api_key=3386c5875b2a009399b57b928eb7b2e5

class Actionwords:
    def __init__(self, test):
        self.test = test

    @staticmethod
    def check_that_the_movie_exists():
        full_request_url = '{}&query={}'.format(SEARCH_MOVIE_QUERY, EXISTING_MOVIE)
        response = get(url=full_request_url)
        movie_title = response.json()['results'][0]['title'].lower()
        assert EXISTING_MOVIE in movie_title
        # movie_id = response.json()['results'][0]['id']
        # movie_details_query = '{}/movie/{}?api_key={}'.format(BASE_URL, movie_id, API_KEY)
        # response = get(url=movie_details_query)


    @staticmethod
    def check_that_the_movie_doesnt_exist():
        full_request_url = '{}&query={}'.format(SEARCH_MOVIE_QUERY, NON_EXISTING_MOVIE)
        response = get(url=full_request_url)
        assert len(response.json()['results']) == 0