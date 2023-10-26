
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
- Ethereum, 2734 tokens
- Bsc, 1831 tokens
- Polygon, 795 tokens
- Arbitrum, 374 tokens
- Avax, 308 tokens
- Ftm, 274 tokens
- Gnosis, 195 tokens
- Optimism, 184 tokens
- Aurora, 112 tokens
- Cronos, 100 tokens
- Moonriver, 64 tokens
- Moonbeam, 59 tokens
- Celo, 33 tokens
- Fuse, 28 tokens
- Base, 23 tokens
- Chains, 22 tokens
- Zkevm, 17 tokens
- Boba, 16 tokens
- Evmos, 7 tokens

## Run aggregation script yourself
Install requirements
```$ pip3 install -r requirements.txt```
Run the script from repo root folder
```python3 aggregate_tokens.py```
## Generate readme.md based on aggregated data
```bash
python generate_readme.py
```
