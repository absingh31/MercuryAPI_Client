#!/usr/bin/env python3

import requests
import urllib.parse

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

    def get_domain(url):
        u = urllib.parse.urlsplit(url)
        return u.netloc

    def get_top_domain(url):
        domain = MercuryAPICall.get_domain(url)
        domain_parts = domain.split('.')
        if len(domain_parts) < 2:
            return domain
        top_domain_parts = 2
        # if a domain's last part is 2 letter long, it must be country name
        if len(domain_parts[-1]) == 2:
            if domain_parts[-1] in ['uk', 'jp']:
                if domain_parts[-2] in ['co', 'ac', 'me', 'gov', 'org', 'net']:
                    top_domain_parts = 3
            else:
                if domain_parts[-2] in ['com', 'org', 'net', 'edu', 'gov']:
                    top_domain_parts = 3
        return '.'.join(domain_parts[-top_domain_parts:])


'''Uncomment these 3 lines to get base domain for any given url'''
# u=input('Enter the url to get base url')
# site_base_url=MercuryAPICall.get_top_domain(u)
# print(site_base_url)







