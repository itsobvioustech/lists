from collections import defaultdict

import httpx

from common import ChainId, Address


def get_coingecko_mcap() -> dict:
    coins = httpx.get('https://api.coingecko.com/api/v3/coins/markets', params={'vs_currency': 'usd'}).json()
    return [coin['id'] for coin in coins]


coingecko_mcap = get_coingecko_mcap()
