
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
- Ethereum, 2739 tokens
- Bsc, 1790 tokens
- Polygon, 792 tokens
- Arbitrum, 435 tokens
- Avax, 368 tokens
- Ftm, 293 tokens
- Gnosis, 178 tokens
- Optimism, 161 tokens
- Aurora, 117 tokens
- Cronos, 102 tokens
- Moonriver, 69 tokens
- Moonbeam, 65 tokens
- Celo, 35 tokens
- Evmos, 33 tokens
- Fuse, 30 tokens
- Base, 24 tokens
- Chains, 22 tokens
- Boba, 20 tokens
- Zkevm, 17 tokens

## Run aggregation script yourself
Install requirements
```$ pip3 install -r requirements.txt```
Run the script from repo root folder
```python3 aggregate_tokens.py```
## Generate readme.md based on aggregated data
```bash
python generate_readme.py
```
