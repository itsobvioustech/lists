from typing import NewType, TypedDict

CHAIN_NAMES_BY_ID = {
    '1': 'ethereum',
    '10': 'optimism',
    '100': 'gnosis',
    '10000': 'smartbch',
    '-1': 'solana',
    '106': 'velas',
    '1024': 'clover',
    '1101': 'zkevm',
    '11297108109': 'palm',
    '122': 'fuse',
    '128': 'heco',
    '1284': 'moonbeam',
    '1285': 'moonriver',
    '1287': 'moonbase',
    '1313161554': 'aurora',
    '137': 'polygon',
    '1666600000': 'harmony',
    '1666700000': 'harmony-testnet',
    '20': 'elastos',
    '25': 'cronos',
    '250': 'ftm',
    '256': 'heco-testnet',
    '288': 'boba',
    '3': 'ropsten',
    '321': 'kcc',
    '361': 'theta',
    '4': 'rinkeby',
    '40': 'telos',
    '4002': 'ftmtest',
    '42': 'kovan',
    '42161': 'arbitrum',
    '42220': 'celo',
    '43113': 'fuji',
    '43114': 'avax',
    '4689': 'iotex',
    '592': 'astar',
    '5': 'goerli',
    '56': 'bsc',
    '1818': 'cube',
    '65': 'okex-testnet',
    '66': 'okex',
    '70': 'hoo',
    '80001': 'mumbai',
    '82': 'meter',
    '88': 'tomochain',
    '97': 'bsc-testnet',
    '9001': 'evmos',
}

Address = NewType('Address', str)

ChainId = NewType('ChainId', str)


class Token(TypedDict):
    symbol: str
    name: str
    address: str
    decimals: str
    chainId: str
    logoURI: str
    coingeckoId: str
    marketCap: int
    marketCapRank: int

NATIVE_ADDR_0xe = "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
NATIVE_ADDR_0x0 = "0x0000000000000000000000000000000000000000"
NATIVE_ADDR_MATIC = "0x0000000000000000000000000000000000001010"
NATIVE_ADDR_CELO = "0x471ece3750da237f93b8e339c536989b8978a438"

NATIVE_ADDRESSES = (NATIVE_ADDR_0xe, NATIVE_ADDR_0x0, NATIVE_ADDR_MATIC, NATIVE_ADDR_CELO)
NATIVE_TOKEN_COIN_GECKO_IDS = {
    '1': 'ethereum',
    '10': 'ethereum',
    '100': 'xdai',
    '10000': 'smartbch',
    '-1': 'solana',
    '106': 'velas',
    '1024': 'clover',
    '1101': 'ethereum',
    '11297108109': 'palm',
    '122': 'fuse',
    '128': 'heco',
    '1284': 'moonbeam',
    '1285': 'moonriver',
    '1287': 'moonbase',
    '1313161554': 'aurora',
    '137': 'matic-network',
    '1666600000': 'harmony',
    '1666700000': 'harmony-testnet',
    '20': 'elastos',
    '25': 'cronos',
    '250': 'fantom',
    '256': 'heco-testnet',
    '288': 'ethereum',
    '3': 'ropsten',
    '321': 'kcc',
    '361': 'theta',
    '4': 'rinkeby',
    '40': 'telos',
    '4002': 'ftmtest',
    '42': 'kovan',
    '42161': 'ethereum',
    '42220': 'celo',
    '43113': 'fuji',
    '43114': 'avalanche-2',
    '4689': 'iotex',
    '592': 'astar',
    '5': 'goerli',
    '56': 'binancecoin',
    '1818': 'cube',
    '65': 'okex-testnet',
    '66': 'okex',
    '70': 'hoo',
    '80001': 'mumbai',
    '82': 'meter',
    '88': 'tomochain',
    '97': 'bsc-testnet',
    '9001': 'evmos',
}

