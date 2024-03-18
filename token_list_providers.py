import asyncio
import json
from collections import defaultdict

import httpx
import os
from web3 import Web3

from coingecko_ids import coingecko_ids
from coingecko_mcap import coingecko_mcap
from common import ChainId, Token, NATIVE_ADDRESSES, NATIVE_TOKEN_COIN_GECKO_IDS


class TokenListProvider:
    name: str
    base_url: str
    chains: dict[ChainId, str]
    _by_chain_id = False
    _get_chain_id_key = False
    _tokens_to_list = False
    # True if tokenlist contains all chains at once and we should filter each chain
    _check_chain_id = False
    headers: dict[str, str]

    @classmethod
    def _filter_tokens(cls, tokens: list[Token], chain_id: str) -> list[Token]:
        res = []
        for token in tokens:
            if not token["address"]:
                continue
            try:
                token["address"] = token["address"].strip()
                if token["address"].startswith("0x"):
                    token["address"] = Web3.to_checksum_address(
                        token["address"])
                cg_id = coingecko_ids.get(chain_id, {}).get(
                    token["address"].lower())
                if cg_id is None and token["address"].lower() in NATIVE_ADDRESSES:
                    cg_id = NATIVE_TOKEN_COIN_GECKO_IDS[chain_id]
                logo = token.get("logoURI") or token.get(
                    "icon") or token.get("image")
                if logo and logo.startswith('//'):
                    logo = 'https:' + logo

                add_token = True
                if cls._check_chain_id:
                    if 'chainId' in token and str(token['chainId']) != chain_id:
                        add_token = False
                    elif 'chain_id' in token and str(token['chain_id']) != chain_id:
                        add_token = False

                if add_token:
                    if 'tokenDecimal' in token:
                        decimals = token['tokenDecimal']
                    else:
                        decimals = token['decimals']

                    t = Token(
                        address=token["address"],
                        symbol=token["symbol"],
                        name=token["name"],
                        decimals=decimals,
                        chainId=chain_id,
                        logoURI=logo,
                        coingeckoId=cg_id,
                        marketCap=coingecko_mcap.get(
                            cg_id, {}).get("market_cap", 0),
                        marketCapRank=coingecko_mcap.get(
                            cg_id, {}).get("market_cap_rank", 0)
                    )
                    res.append(t)
            except Exception as exc:
                print(chain_id, token["address"], exc, token)
        return res

    @classmethod
    async def get_tokenlists(cls) -> dict[str, dict[ChainId, list[Token]]]:
        res: dict[ChainId, list[Token]] = defaultdict(list)

        for chain_id, chain_name in cls.chains.items():
            try:
                resp = await httpx.AsyncClient().get(
                    cls.base_url.format(
                        chain_id if cls._by_chain_id else chain_name),
                    headers=cls.headers if hasattr(cls, "headers") else None
                )
            except httpx.ReadTimeout:
                await asyncio.sleep(0.5)
                continue
            num_retries = 0
            while resp.status_code != 200:
                if num_retries > 60:
                    raise Exception(
                        f"failed to get tokenlits {cls.base_url} after {num_retries} retries")
                sleep_time = int(resp.headers.get("Retry-After", 1))
                num_retries += 1
                print(
                    f"[{cls.name}] {chain_id} {chain_name} waiting {sleep_time} seconds")
                await asyncio.sleep(sleep_time)
                resp = await httpx.AsyncClient().get(
                    cls.base_url.format(
                        chain_id if cls._by_chain_id else chain_name),
                    headers=cls.headers if hasattr(cls, "headers") else None
                )

            try:
                tokenlist = resp.json()
            except:
                tokenlist = json.loads(resp.text)

            if "tokens" in tokenlist:
                tokens = tokenlist["tokens"]
            elif "data" in tokenlist:
                tokens = tokenlist["data"]
            elif "results" in tokenlist:
                tokens = tokenlist["results"]
            else:
                tokens = tokenlist

            if cls._get_chain_id_key and str(chain_id) in tokens:
                tokens = tokens[str(chain_id)]

            if cls._tokens_to_list:
                tokens = list(tokens.values())

            res[chain_id] = cls._filter_tokens(tokens, chain_id)
            print(f"[{cls.name}] {chain_id} {chain_name} OK")
        return {cls.name: res}


class CoinGecko(TokenListProvider):
    name = "coingecko"
    base_url = "https://tokens.coingecko.com/{}/all.json"
    chains = {
        # "592": "astar",
        "1284": "moonbeam",
        # "361": "theta",
        # "70": "hoo-smart-chain",
        "42161": "arbitrum-one",
        "8453": "base",
        "56": "binance-smart-chain",
        # "66": "okex-chain",
        "250": "fantom",
        # "88": "tomochain",
        # "82": "meter",
        "42220": "celo",
        "10": "optimistic-ethereum",
        "137": "polygon-pos",
        "1101": "polygon-zkevm",
        "43114": "avalanche",
        "1285": "moonriver",
        "25": "cronos",
        "106": "velas",
        "288": "boba",
        # "10000": "smartbch",
        "1313161554": "aurora",
        # "1666600000": "harmony-shard-0",
        "100": "xdai",
        "1": "ethereum",
        # "-1": "solana",
        "9001": "evmos",
        # sora
    }


class Uniswap(TokenListProvider):
    name = "uniswap"
    base_url = "https://raw.githubusercontent.com/Uniswap/default-token-list/main/src/tokens/{}.json"
    chains = {
        "42161": "arbitrum",
        "43114": "avalanche",
        "8453": "base",
        # "5": "goerli",
        # "42": "kovan",
        "1": "mainnet",
        # "80001": "mumbai",
        "137": "polygon",
        # "4": "rinkeby",
        # "3": "ropsten",
    }


class Sushiswap(TokenListProvider):
    name = "sushiswap"
    base_url = "https://raw.githubusercontent.com/sushiswap/list/master/lists/token-lists/default-token-list/tokens/{}.json"
    # https://raw.githubusercontent.com/sushiswap/default-token-list/master/tokens/{}.json
    chains = {
        "42161": "arbitrum",
        "43114": "avalanche",
        # "97": "bsc-testnet",
        "8453": "base",
        "56": "bsc",
        "42220": "celo",
        # "1024": "clover",
        "1": "ethereum",
        # "4002": "fantom-testnet",
        "250": "fantom",
        # "43113": "fuji",
        "122": "fuse",
        # "5": "goerli",
        # "1666700000": "harmony-testnet",
        # "1666600000": "harmony",
        # "256": "heco-testnet",
        # "128": "heco",
        # "42": "kovan",
        # "80001": "matic-testnet",
        # "1287": "moonbase",
        "1285": "moonriver",
        "1284": "moonbeam",
        # "65": "okex-testnet",
        # "66": "okex",
        # "11297108109": "palm",
        "137": "polygon",
        # "4": "rinkeby",
        # "3": "ropsten",
        # "40": "telos",
        "100": "xdai",
    }


class OneInch(TokenListProvider):
    name = "1inch"
    base_url = "https://api.1inch.dev/token/v1.2/{}/token-list"
    chains = {
        "1313161554": "aurora",
        "1": "ethereum",
        "10": "optimism",
        "8453": "base",
        "56": "bsc",
        "250": "fantom",
        "100": "gnosis",
        "137": "polygon",
        "43114": "avalanche",
        "42161": "arbitrum",
    }
    _by_chain_id = True
    # _tokens_to_list = True
    # PLEASE GET AUTH TOKEN FROM 1INCH - https://portal.1inch.dev/dashboard
    headers = {
        "Authorization": f"Bearer {os.environ['ONEINCH_API_KEY']}"
    }


class OpenOcean(TokenListProvider):
    # TODO: maybe more, check all ids from coingecko
    name = "openocean"
    base_url = "https://open-api.openocean.finance/v1/cross/tokenList?chainId={}"
    chains = {
        "42161": "arbitrum-one",
        "43114": "avalanche",
        "56": "binance-smart-chain",
        # "66": "okex-chain",
        "250": "fantom",
        "10": "optimistic-ethereum",
        "137": "polygon-pos",
        "288": "boba",
        "100": "xdai-gnosis",
        # "128": "heco",
        "1": "ethereum",
    }
    _by_chain_id = True


class ElkFinance(TokenListProvider):
    name = "elkfinance"
    base_url = "https://raw.githubusercontent.com/elkfinance/tokens/main/{}.tokenlist.json"
    chains = {
        # "42161": "farms",
        "43114": "avax",
        "56": "bsc",
        "25": "cronos",
        # "20": "elastos",
        "1": "ethereum",
        "250": "ftm",
        # "4002": "ftmtest",
        # "43113": "fuji",
        "122": "fuse",
        # "1666600000": "harmony",
        # "128": "heco",
        # "70": "hoo",
        # "4689": "iotex",
        # "321": "kcc",
        "137": "matic",
        "1285": "moonriver",
        # "80001": "mumbai",
        # "66": "okex",
        # "40": "telos",
        "100": "xdai"
    }
    # "all", "top"


class RefFinanceTokenLists(TokenListProvider):
    # unusual format
    base_url = "https://indexer.ref-finance.net/list-token"


class OneSolTokenLists(TokenListProvider):
    name = "1sol"
    base_url = "https://raw.githubusercontent.com/1sol-io/token-list/fb6336f63b1511c095bd5160277983a6ad3c8aa5/src/tokens/solana.tokenlist.json"
    chains = {
        "-1": "solana"
    }


class QuickSwap(TokenListProvider):
    name = "quickswap"
    base_url = "https://raw.githubusercontent.com/sameepsi/quickswap-default-token-list/master/src/tokens/mainnet.json"
    chains = {
        "137": "polygon"
    }


class QuickSwapZkEvm(TokenListProvider):
    name = "quickzkevm"
    base_url = "https://raw.githubusercontent.com/sameepsi/quickswap-default-token-list/master/src/tokens/zkevm.json"
    chains = {
        "1101": "zkevm"
    }


class XQuickSwapZkEvm(TokenListProvider):
    name = "xquickzkevm"
    base_url = "https://raw.githubusercontent.com/sameepsi/quickswap-default-token-list/master/src/tokens/zkevm.json"
    chains = {
        "1101": "zkevm"
    }


class FuseSwapTokenLists(TokenListProvider):
    name = "fuseswap"
    base_url = "https://raw.githubusercontent.com/fuseio/fuseswap-default-token-list/master/src/tokens/fuse.json"
    chains = {
        "122": "fuse"
    }


class TrisolarisLabsLists(TokenListProvider):
    name = "trisolaris"
    base_url = "https://raw.githubusercontent.com/trisolaris-labs/tokens/master/lists/{}/list.json"
    chains = {
        "1313161554": "1313161554",
    }


class RubicLists(TokenListProvider):
    name = "rubic"
    base_url = "https://tokens.rubic.exchange/api/v1/tokens/?pageSize=200&network={}"
    chains = {
        # "-2": "near",
        # "-1": "solana",
        "1": "ethereum",
        "25": "cronos",
        # '40': 'telos',
        "56": "binance-smart-chain",
        "100": "xdai",
        "137": "polygon",
        "250": "fantom",
        "1284": "moonbeam",
        "1285": "moonriver",
        "42161": "arbitrum",
        "43114": "avalanche",
        "1313161554": "aurora",
        # "1666600000": "harmony",
    }


class CronaSwapLists(TokenListProvider):
    name = "cronaswap"
    base_url = "https://raw.githubusercontent.com/cronaswap/default-token-list/main/assets/tokens/cronos.json"
    chains = {'25': 'cronos'}


class Ubeswap(TokenListProvider):
    name = "ubeswap"
    base_url = "https://raw.githubusercontent.com/Ubeswap/default-token-list/master/ubeswap.token-list.json"
    chains = {'42220': 'celo'}


class OolongSwap(TokenListProvider):
    name = "oolongswap"
    base_url = "https://raw.githubusercontent.com/OolongSwap/boba-community-token-list/main/src/tokens/boba.json"
    chains = {'288': 'boba'}


class Multichain(TokenListProvider):
    name = 'multichain'
    base_url = "https://bridgeapi.anyswap.exchange/v4/poollist/{}"
    chains = {'592': '592'}
    _tokens_to_list = True


class XyFinance(TokenListProvider):
    name = "xyfinance"
    base_url = "https://token-list-v2.xy.finance/"
    chains = {
        '1': '1',
        '56': '56',
        '137': '137',
        '250': '250',
        '25': '25',
        '43114': '43114',
        '42161': '42161',
        '10': '10',
        '1285': '1285',
        '592': '592',
        '321': '321',
        '1818': '1818',
    }
    _check_chain_id = True


class MojitoSwap(TokenListProvider):
    name = "mojitoswap"
    base_url = "https://raw.githubusercontent.com/MojitoFinance/mjtTokenList/461d2ca814d12c37516b986fabfcd21446283ed7/mjtTokenList.json"
    chains = {'321': '321'}


class CapricornFinance(TokenListProvider):
    name = "capricorn_finance"
    base_url = "https://raw.githubusercontent.com/capricorn-finance/info-blist/main/list.json"
    chains = {'1818': '1818'}


class Lifinance(TokenListProvider):
    name = "lifinance"
    base_url = "https://li.quest/v1/tokens?chains={}"
    _get_chain_id_key = True

    chains = {
        '1': '1',
        '10': '10',
        # '25': '25', #Cronos
        '56': '56',
        # '66': '66',
        '100': '100',
        # '106': '106', #Velas
        '122': '122',
        '137': '137',
        '250': '250',
        '288': '288',
        '1284': '1284',
        '1285': '1285',
        # '9001': '9001',
        '42161': '42161',
        # '42220': '42220', #Celo
        '43114': '43114',
        '1313161554': '1313161554',
        # '1666600000': '1666600000',
    }

# Duplicating LIFI to get all tokens for these chains


class xLifinance(TokenListProvider):
    name = "xlifinance"
    base_url = "https://li.quest/v1/tokens?chains={}"
    _get_chain_id_key = True

    chains = {
        # '106': '106', #Cronos
        '122': '122',
        '288': '288',
        # '9001': '9001',
    }


class Dfyn(TokenListProvider):
    name = "dfyn"
    base_url = "https://raw.githubusercontent.com/dfyn/new-host/main/list-token.tokenlist.json"
    _check_chain_id = True

    chains = {
        '1': '1',
        '10': '10',
        '25': '25',
        '56': '56',
        '137': '137',
        '250': '250',
        '43114': '43114',
        '1666600000': '1666600000',
    }


class PancakeSwap(TokenListProvider):
    name = "pancake"
    base_url = "https://tokens.pancakeswap.finance/pancakeswap-extended.json"
    _check_chain_id = True

    chains = {'56': '56'}


class Pangolin(TokenListProvider):
    name = "pangolin"
    base_url = "https://raw.githubusercontent.com/pangolindex/tokenlists/main/pangolin.tokenlist.json"
    _check_chain_id = True

    chains = {'43114': 43114}


class ArbitrumBridge(TokenListProvider):
    name = "arbitrum_bridge"
    base_url = "https://bridge.arbitrum.io/token-list-42161.json"
    _check_chain_id = True

    chains = {'42161': 42161, "1": 1}


class Optimism(TokenListProvider):
    name = "optimism"
    base_url = "https://static.optimism.io/optimism.tokenlist.json"
    _check_chain_id = True

    chains = {'1': 1, '10': 10, }


class SpookySwap(TokenListProvider):
    name = "SpookySwap"
    base_url = "https://raw.githubusercontent.com/SpookySwap/spooky-info/master/src/constants/token/spookyswap.json"
    _check_chain_id = True

    chains = {'250': 250}


class RouterProtocol(TokenListProvider):
    name = "RouterProtocol"
    base_url = "https://raw.githubusercontent.com/router-protocol/reserve-asset-list/main/router-reserve-asset.json"
    _check_chain_id = True

    chains = {
        '1': 1,
        '10': 10,
        '25': 25,
        '56': 56,
        '137': 137,
        '250': 250,
        '42161': 42161,
        '1313161554': 1313161554,
        '1666600000': 1666600000,
    }


# Sorting order of this is important for token icons, the last in the list will be picked
# Prefer 1inch Icons over other token icons

tokenlists_providers = [
    # OneSolTokenLists,
    FuseSwapTokenLists,
    TrisolarisLabsLists,
    SpookySwap,
    # MojitoSwap,
    CronaSwapLists,
    Ubeswap,
    OolongSwap,
    # CapricornFinance,
    # Dfyn,
    # RouterProtocol,
    # Multichain, # for Astar
    xLifinance,
    Lifinance,
    Pangolin,
    XyFinance,
    Optimism,
    # ArbitrumBridge,
    CoinGecko,
    RubicLists,
    ElkFinance,
    PancakeSwap,
    Sushiswap,
    OpenOcean,
    QuickSwapZkEvm,
    XQuickSwapZkEvm,
    Uniswap,
    OneInch,
    QuickSwap,
]
