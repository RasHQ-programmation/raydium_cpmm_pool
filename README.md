# Liquidity Pool State Analyzer

The CPMM Liquidity Pool State is a Python library that provides tools for analyzing the state of raydium liquidity pools in solana blockchain. This library allows users to fetch, parse, and analyze various aspects of liquidity pool states, including configuration details, token vaults, LP minting, fees, and observations.

## Features

- Fetch and parse raydium CPMM pool state data from solana blockchain networks.
- Analyze configuration details such as AMM (Automated Market Maker) settings and fee rates.
- Retrieve token vault information including balances and fees.
- Calculate token prices based on vault amounts and fees.
- Access observation data to track historical changes in pool state.

## Usage

Here's a basic example demonstrating how to use the library to analyze a liquidity pool's state:

```python
from solana.rpc.api import Client
from src.state import PoolState

# Initialize a Solana client (using solana-py)
client = Client("https://api.mainnet-beta.solana.com")
lp_address = "7JuwJuNU88gurFnyWeiyGKbFmExMWcmRZntn9imEzdny" #USING SOL / USDC

pool_state = PoolState(pool_state_address, client)

# Access pool state attributes and methods
print("Token 0 vault address:", pool_state.token_0_vault)
print("Token 1 vault address:", pool_state.token_1_vault)

# Get token prices
token_0_price, token_1_price = pool_state.token_price_x32()
print("Token 0 price:", token_0_price)
print("Token 1 price:", token_1_price)
```
## Contributing
Contributions to the Liquidity Pool State are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License
This project is licensed under the MIT License.
