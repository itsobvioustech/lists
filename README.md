
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
- Ethereum, 2805 tokens
- Bsc, 1867 tokens
- Polygon, 804 tokens
- Arbitrum, 441 tokens
- Avax, 371 tokens
- Ftm, 298 tokens
- Gnosis, 178 tokens
- Optimism, 165 tokens
- Aurora, 117 tokens
- Cronos, 102 tokens
- Moonriver, 72 tokens
- Moonbeam, 67 tokens
- Celo, 36 tokens
- Evmos, 33 tokens
- Fuse, 30 tokens
- Base, 24 tokens
- Chains, 22 tokens
- Boba, 20 tokens
- Zkevm, 18 tokens

## Run aggregation script yourself
Install requirements
```$ pip3 install -r requirements.txt```
Run the script from repo root folder
```python3 aggregate_tokens.py```
## Generate readme.md based on aggregated data
```bash
python generate_readme.py
```
