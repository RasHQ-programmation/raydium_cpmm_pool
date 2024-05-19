from solana.rpc.api import Client
from src.state import PoolState

# Initialize a Solana client (using solana-py)
client = Client("https://api.mainnet-beta.solana.com")
lp_address = "7JuwJuNU88gurFnyWeiyGKbFmExMWcmRZntn9imEzdny" #USING SOL / USDC

# Fetch and parse the AMM data
pool_state = PoolState(lp_address,client)

print(pool_state.data)
print(pool_state.amm_cfg)
print(pool_state.observations)
print(pool_state.vault_amout)
print(pool_state.vault_amount_without_fees)
#TODO fix token_price
#print(pool_state.token_price_x32())
