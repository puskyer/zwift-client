# -*- coding: utf-8 -*-
import requests

from .error import RequestException


class Request:
    """Class for handling requests."""
    DEFAULT_HEADERS = {"User-Agent": "Zwift/115 CFNetwork/758.0.2 Darwin/15.0.0"}

    def __init__(self, get_access_token):
        self.get_access_token = get_access_token

    def get_headers(self, accept_type):
        headers = {
            "Accept": accept_type,
            "Authorization": "Bearer " + self.get_access_token()
        }
        headers.update(self.DEFAULT_HEADERS)
        return headers

    def json(self, url):
        headers = self.get_headers(accept_type='application/json')
        resp = requests.get('https://us-or-rly101.zwift.com' + url, headers=headers)
        if not resp.ok:
            raise RequestException("{} - {}".format(resp.status_code, resp.reason))
        return resp.json()

    def protobuf(self, url):
        headers = self.get_headers(accept_type='application/x-protobuf-lite')
        resp = requests.get('https://us-or-rly101.zwift.com' + url, headers=headers)
        if not resp.ok:
            raise RequestException("{} - {}".format(resp.status_code, resp.reason))
        return resp.content
