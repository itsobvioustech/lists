
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
- Ethereum, 2328 tokens
- Bsc, 910 tokens
- Polygon, 716 tokens
- Arbitrum, 325 tokens
- Avax, 291 tokens
- Ftm, 262 tokens
- Gnosis, 185 tokens
- Optimism, 165 tokens
- Aurora, 113 tokens
- Cronos, 101 tokens
- Moonriver, 64 tokens
- Moonbeam, 54 tokens
- Celo, 36 tokens
- Base, 22 tokens
- Chains, 22 tokens
- Fuse, 18 tokens
- Zkevm, 17 tokens
- Boba, 13 tokens
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
