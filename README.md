
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
- Ethereum, 3043 tokens
- Bsc, 1966 tokens
- Polygon, 826 tokens
- Arbitrum, 457 tokens
- Avax, 384 tokens
- Ftm, 297 tokens
- Optimism, 171 tokens
- Gnosis, 171 tokens
- Aurora, 119 tokens
- Cronos, 102 tokens
- Moonriver, 68 tokens
- Moonbeam, 67 tokens
- Celo, 37 tokens
- Fuse, 31 tokens
- Evmos, 31 tokens
- Base, 26 tokens
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
