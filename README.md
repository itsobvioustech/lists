
## Multi-chain token list 
We collect many tokenlists from many providers, then we aggregate them by chains and tokens addresses. 
For each token we check whether it is listed in 2 or more tokenlists from different providers. If so, 
we add it to our trusted tokenlist.

## Providers
We collect tokenlists from github repos or open APIs from various platforms, currently:
- [CoinGecko](https://www.coingecko.com/)
- [1inch](https://app.1inch.io/)
- [Uniswap](https://uniswap.org/)
- [Sushiswap](https://www.sushi.com/)
- [OpenOcean](https://openocean.finance/)
- [QuickSwap](https://quickswap.exchange/#/swap)

## Chains with trusted tokens
Here are chains presented in our tokenlists with current token count. You can find out more in `/tokens` folder.
Token counts are approximate and may vary as providers update their tokenlists.
- Ethereum, 1562 tokens
- Bsc, 1016 tokens
- Polygon, 590 tokens
- Avax, 315 tokens
- Ftm, 311 tokens
- Gnosis, 261 tokens
- Arbitrum, 208 tokens
- Cronos, 142 tokens
- Aurora, 131 tokens
- Optimism, 108 tokens
- Moonriver, 81 tokens
- Moonbeam, 63 tokens
- Celo, 42 tokens
- Fuse, 20 tokens
- Velas, 13 tokens
- Evmos, 11 tokens

## Run aggregation script yourself
Install requirements
```$ pip3 install -r requirements.txt```
Run the script from repo root folder
```python3 aggregate_tokens.py```
## Generate readme.md based on aggregated data
```bash
python generate_readme.py
```
