import asyncio
import json
from collections import defaultdict

import httpx
from web3 import Web3

from common import ChainId, Address, NATIVE_ADDRESSES, NATIVE_ADDR_0x0, Token, CHAIN_NAMES_BY_ID
from token_list_providers import tokenlists_providers

TOKENLISTS_FOLDER = "tokens"


async def collect_trusted_tokens() -> dict[ChainId, dict[Address, Token]]:
    data = await asyncio.gather(*[provider.get_tokenlists() for provider in tokenlists_providers])
    provider_data: dict[str, dict[ChainId, list[Token]]] = {}
    for prov in data:
        provider_data |= prov

    res = defaultdict(dict)
    for provider_name, tokens_by_chains in provider_data.items():
        for chain_id, tokens in tokens_by_chains.items():
            for token in tokens:
                token['chainId'] = int(token['chainId'])
                addr = token["address"].strip().lower()
                token["address"] = addr
                if addr in NATIVE_ADDRESSES:  # skip native tokens
                    addr = NATIVE_ADDR_0x0
                    token['address'] = addr
                # if addr.startswith('0x'):
                #     token['address'] = Web3.toChecksumAddress(addr)
                if addr in res[chain_id]:
                    if "listedIn" in res[chain_id][addr]:
                        res[chain_id][addr] |= token
                        if provider_name not in res[chain_id][addr]["listedIn"]:
                            res[chain_id][addr]["listedIn"].append(
                                provider_name)
                    else:
                        res[chain_id][addr]["listedIn"] = [provider_name]
                else:
                    res[chain_id][addr] = token
                    res[chain_id][addr]["listedIn"] = [provider_name]

    trusted = {
        chain_id: {addr: token for addr, token in tokens.items() if len(token["listedIn"]) > 1} for
        chain_id, tokens in res.items()
    }
    trusted = {k: v for k, v in trusted.items() if len(v) > 0}
    # trusted = {k: list(sorted(v.values(), key=lambda x: x['marketCap'], reverse=True)) for k, v in trusted.items()}
    print("dumping all chains file")
    for chain_id, tokens in trusted.items():
        for addr, token in tokens.items():
            del token["listedIn"]
            del token["marketCap"]
        
        filename = f"{TOKENLISTS_FOLDER}/{CHAIN_NAMES_BY_ID[chain_id]}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(tokens, f, ensure_ascii=False)
    print("dumping all tokens file")
    with open(f"{TOKENLISTS_FOLDER}/all.json", "w", encoding="utf-8") as f:
        json.dump(trusted, f, ensure_ascii=False)

    # token_hashed = {k: {item['address']:item for item in v} for k, v in trusted.items()}
    # with open(f"{TOKENLISTS_FOLDER}/all_hashed.json", "w", encoding="utf-8") as f:
    #     json.dump(token_hashed, f, ensure_ascii=False)

    print("collected trusted tokens")
    return trusted


if __name__ == "__main__":
    asyncio.run(collect_trusted_tokens())
