
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
- Ethereum, 3311 tokens
- Bsc, 2043 tokens
- Polygon, 850 tokens
- Arbitrum, 488 tokens
- Base, 414 tokens
- Avax, 397 tokens
- Ftm, 306 tokens
- Optimism, 183 tokens
- Gnosis, 171 tokens
- Cronos, 121 tokens
- Aurora, 119 tokens
- Moonbeam, 69 tokens
- Moonriver, 69 tokens
- Celo, 37 tokens
- Fuse, 35 tokens
- Evmos, 34 tokens
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
