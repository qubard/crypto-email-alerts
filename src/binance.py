from requests import get
import config

"""
Example usage (fetch the price of BTCUSDT):

api = API()
api.fetch_ticker_pairs()
btc_price = api.price('BTCUSDT')

print(btc_price)
"""

class API:
    def fetch_json(self):
        r = get(config.api_url)

        if r.status_code is not 200:
            return None

        json = r.json()
        return json

    def json_to_dict(self, json):
        pairs = {}
        for pair in json:
            label = pair['symbol']
            pairs[label] = pair

        return pairs

    def fetch_ticker_pairs(self):
        json = API.fetch_json(self)

        if json is None:
            return None

        self.pairs = self.json_to_dict(json)
        return self.pairs

    """
    Gets the last price of a pairing
    """
    def price(self, pair):
        return float(self.pairs[pair]['lastPrice'])
