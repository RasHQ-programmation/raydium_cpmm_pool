
---

# CPMM Raydium Liquidity Pool State Analyzer

The **CPMM Raydium Solana Liquidity Pool State Analyzer** is a powerful Python library designed for analyzing the state of Raydium liquidity pools on the Solana blockchain. This tool provides comprehensive functionality to fetch, parse, and analyze various aspects of liquidity pool states, enabling users to gain deep insights into the configuration, token vaults, LP minting, fees, and historical observations.

## Features

- **Fetch and Parse Data**: Retrieve detailed Raydium CPMM pool state data from Solana blockchain networks.
- **Configuration Analysis**: Examine AMM (Automated Market Maker) settings, fee rates, and other configuration details.
- **Token Vault Information**: Access balances and fees associated with token vaults.
- **Price Calculation**: Determine token prices based on vault amounts and fees.
- **Historical Data**: Track and analyze historical changes in pool states through observation data.
- **Slippage Tolerance**: Calculate minimal output amounts according to specified slippage tolerance.

## Installation

To install the library, use:

```sh
pip install your-package-name
```

## Usage

Here's a basic example demonstrating how to use the library to analyze a liquidity pool's state:

```python
from solana.rpc.api import Client
from src.state import PoolState

# Initialize a Solana client using solana-py
client = Client("https://api.mainnet-beta.solana.com")
lp_address = "7JuwJuNU88gurFnyWeiyGKbFmExMWcmRZntn9imEzdny"  # SOL / USDC Pool Address

# Fetch and parse the AMM data
pool_state = PoolState(lp_address, client)

# Print relevant pool state information
print("Pool Data:", pool_state.data)
print("AMM Configuration:", pool_state.amm_cfg)
print("Observations Index:", pool_state.observations['observation_index'])
print("First Two Observations:", pool_state.observations['observations'][:2])
print("Vault Amount:", pool_state.vault_amout)
print("Vault Amount Without Fees:", pool_state.vault_amount_without_fees)
```

## Contributing

We welcome contributions to the **CPMM Raydium Liquidity Pool State Analyzer**! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/RasHQ-programmation/raydium_cpmm_pool/).

## How to Support

Feel free to support this open-source initiative:

- **SOL**: 4X3aRmzpw65cJwJSkVDqxsBUzkXxsnyYxTcRXm9aWMkU
- **ETH**: 0x86B9f7eaD77467bCEd565a017423835B33baFC45
- **POLY**: 0x86B9f7eaD77467bCEd565a017423835B33baFC45
- **BTC Taproot**: bc1pe02yq7ee38real7lxfmaf2tvatqsj47hc9knlgv0u3syt5rnqrrqle4m46
- **BTC Segwit**: bc1ql9ww94rgexallzqwp29ueyhq55e78vwta96d9a

## Connect with Me

- **Twitter**: [LaTonzaille](https://x.com/LaTonzaille)
- **Discord**: rashq

## License

This project is licensed under the MIT License. See the [LICENSE] file for more details.

---
