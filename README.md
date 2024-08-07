
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
- Ethereum, 2761 tokens
- Bsc, 1669 tokens
- Base, 1368 tokens
- Polygon, 790 tokens
- Arbitrum, 539 tokens
- Avax, 393 tokens
- Ftm, 289 tokens
- Gnosis, 242 tokens
- Optimism, 154 tokens
- Cronos, 146 tokens
- Aurora, 125 tokens
- Moonbeam, 68 tokens
- Moonriver, 64 tokens
- Fuse, 41 tokens
- Celo, 39 tokens
- Evmos, 34 tokens
- Chains, 22 tokens
- Boba, 21 tokens
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
