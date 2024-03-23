
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
- Ethereum, 3304 tokens
- Bsc, 2040 tokens
- Polygon, 851 tokens
- Arbitrum, 490 tokens
- Base, 435 tokens
- Avax, 395 tokens
- Ftm, 307 tokens
- Optimism, 185 tokens
- Gnosis, 171 tokens
- Cronos, 121 tokens
- Aurora, 119 tokens
- Moonriver, 69 tokens
- Moonbeam, 68 tokens
- Celo, 37 tokens
- Evmos, 34 tokens
- Fuse, 25 tokens
- Chains, 22 tokens
- Zkevm, 20 tokens
- Boba, 20 tokens

## Run aggregation script yourself
Install requirements
```$ pip3 install -r requirements.txt```
Run the script from repo root folder
```python3 aggregate_tokens.py```
## Generate readme.md based on aggregated data
```bash
python generate_readme.py
```
