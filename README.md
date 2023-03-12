
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
- Ethereum, 1593 tokens
- Bsc, 1059 tokens
- Polygon, 655 tokens
- Ftm, 325 tokens
- Avax, 323 tokens
- Gnosis, 289 tokens
- Arbitrum, 246 tokens
- Cronos, 136 tokens
- Aurora, 133 tokens
- Optimism, 122 tokens
- Moonriver, 102 tokens
- Moonbeam, 80 tokens
- Celo, 71 tokens
- Evmos, 49 tokens
- Fuse, 32 tokens
- Velas, 13 tokens

## Run aggregation script yourself
Install requirements
```$ pip3 install -r requirements.txt```
Run the script from repo root folder
```python3 aggregate_tokens.py```
## Generate readme.md based on aggregated data
```bash
python generate_readme.py
```
