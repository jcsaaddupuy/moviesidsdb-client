# -*- coding: utf-8 -*-

import os
import requests
from osdbinfos import OpenSutitles


class MoviesIdsDbError(Exception):
    pass


class MoviesIdsDbServerError(MoviesIdsDbError):
    pass


class MoviesIdsDb(object):

    ENDPOINTS = {
        'movie.identify': '/api/movies/identify?hash={hash}&size={size}'
    }

    def __init__(self, host='moviesidsdb.com'):
        self.host = host
        self.scheme = 'http://'
        self.osdb = OpenSutitles()

    def _get_url_(self, url_part):
        return self.scheme + self.host + url_part

    def identify(self, path, timeout=None):

        # compute hash + size
        _hash = self.osdb.get_hash(path)
        _size = os.path.getsize(path)
        endpoint = self.ENDPOINTS['movie.identify'].format(hash=_hash,
                                                           size=_size)

        result = requests.get(self._get_url_(endpoint), timeout=timeout)
        if result.status_code == 200:
            return result.json()
        elif result.status_code == 404:
            return None
        elif result.status_code == 500:
            raise MoviesIdsDbServerError()
