
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
- Ethereum, 3418 tokens
- Bsc, 2038 tokens
- Base, 1106 tokens
- Polygon, 848 tokens
- Arbitrum, 534 tokens
- Avax, 400 tokens
- Ftm, 303 tokens
- Gnosis, 246 tokens
- Optimism, 196 tokens
- Cronos, 145 tokens
- Aurora, 124 tokens
- Moonriver, 71 tokens
- Moonbeam, 71 tokens
- Celo, 40 tokens
- Fuse, 37 tokens
- Evmos, 34 tokens
- Chains, 22 tokens
- Boba, 22 tokens
- Zkevm, 20 tokens

## Run aggregation script yourself
Install requirements
```$ pip3 install -r requirements.txt```
Run the script from repo root folder
```python3 aggregate_tokens.py```
## Generate readme.md based on aggregated data
```bash
python generate_readme.py
```
