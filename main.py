from solana.rpc.api import Client
from src.state import PoolState
from utils.calculations import calculate_min_output

# Initialize a Solana client using solana-py
client = Client("https://api.mainnet-beta.solana.com")
lp_address = "7JuwJuNU88gurFnyWeiyGKbFmExMWcmRZntn9imEzdny"  # USDC / SOL Pool Address

# Fetch and parse the AMM data
pool_state = PoolState(lp_address, client)

# Print relevant pool state information
print("Pool Data:", pool_state.data)
print("AMM Configuration:", pool_state.amm_cfg)
print("Observations Index:", pool_state.observations['observation_index'])
print("Observations:", pool_state.observations['observations'][:2])
print("Vault Amount:", pool_state.vault_amout)
print("Vault Amount Without Fees:", pool_state.vault_amount_without_fees)

# Intention: Buy USDC with 0.00001 SOL
sol_balance_ui = 0.00001

# Calculate the minimal output of USDC we can get for the given SOL, considering a 5% slippage limit
minimal_usdc_output_scaled, minimal_usdc_output_atomic = calculate_min_output(pool_state, sol_balance_ui, 'BUY', 0.95)

# Print the expected minimal USDC output after considering slippage
print("Minimal USDC Output (Scaled):", minimal_usdc_output_scaled)
print("Minimal USDC Output (Atomic):", minimal_usdc_output_atomic)

# Assume we get the minimal USDC output as calculated
usdc_balance_ui = minimal_usdc_output_scaled

# Calculate the minimal output of SOL we can get if we sell the obtained USDC, considering a 5% slippage limit
minimal_sol_output_scaled, minimal_sol_output_atomic = calculate_min_output(pool_state, usdc_balance_ui, 'SELL', 0.95)

# Print the expected minimal SOL output after considering slippage
print("Minimal SOL Output (Scaled):", minimal_sol_output_scaled)
print("Minimal SOL Output (Atomic):", minimal_sol_output_atomic)
