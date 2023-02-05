
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
- Ethereum, 1579 tokens
- Bsc, 1027 tokens
- Polygon, 593 tokens
- Avax, 314 tokens
- Ftm, 310 tokens
- Gnosis, 261 tokens
- Arbitrum, 213 tokens
- Cronos, 141 tokens
- Aurora, 132 tokens
- Optimism, 110 tokens
- Moonriver, 81 tokens
- Moonbeam, 64 tokens
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
