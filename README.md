
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
- Ethereum, 2907 tokens
- Bsc, 1986 tokens
- Polygon, 824 tokens
- Arbitrum, 394 tokens
- Avax, 318 tokens
- Ftm, 282 tokens
- Gnosis, 199 tokens
- Optimism, 190 tokens
- Aurora, 113 tokens
- Cronos, 100 tokens
- Moonriver, 66 tokens
- Moonbeam, 48 tokens
- Celo, 33 tokens
- Fuse, 29 tokens
- Base, 23 tokens
- Chains, 22 tokens
- Evmos, 18 tokens
- Zkevm, 17 tokens
- Boba, 16 tokens

## Run aggregation script yourself
Install requirements
```$ pip3 install -r requirements.txt```
Run the script from repo root folder
```python3 aggregate_tokens.py```
## Generate readme.md based on aggregated data
```bash
python generate_readme.py
```
