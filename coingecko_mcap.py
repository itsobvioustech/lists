from collections import defaultdict

import httpx

from common import ChainId, Address


def get_coingecko_mcap() -> dict[str, dict]:
    coins = [httpx.get('https://api.coingecko.com/api/v3/coins/markets', params={'vs_currency': 'usd', 'per_page': 250, 'page': page}).json() for page in range(1,4)]
    # print(coins)
    market_cap_data: dict[str, dict] = {}
    for coin in coins:
        for coin_data in coin:
            market_cap_data[coin_data['id']] = coin_data
    return market_cap_data

coingecko_mcap = get_coingecko_mcap()