import decimal

import requests
import config


class API(object):

    def __init__(self, key='', secret=''):
        self.key = key
        self.secret = secret
        self.uri = 'https://api.kraken.com'
        self.apiversion = '0'
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'pytrader/' + config.pytrader_version
        })
        self.response = None
        self._json_options = {}
        return

    def fetch_ohlc(self, pair: str, since: decimal.Decimal):
        url = f"{self.uri}/{self.apiversion}/public/OHLC"
        data = {'pair': pair, 'since': since}

        self.response = self.session.post(url, data=data, timeout=config.query_timeout, headers=None)
        if self.response.status_code not in (200, 201, 202):
            self.response.raise_for_status()

        return self.response.json(**self._json_options)