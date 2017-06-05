#!/usr/bin/env python3
import requests

import exceptions


class MercuryAPICall:
    def __init__(self, private_api_key):
        self.private_api_key = private_api_key
        self._headers = {'x-api-key': self.private_api_key}

    def parse_article(self, article_url):
        #Parse article with URL
        api_request = 'https://mercury.postlight.com/parser?url={}'.format(article_url)
        response = requests.get(api_request, headers=self._headers)

        if response.status_code == 401:
            raise exceptions.InvalidApiKey('{} Unauthorized'.format(response.status_code))

        return response






