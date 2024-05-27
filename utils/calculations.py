
from src.state import PoolState


def calculate_min_output(pool_state : PoolState, balance_ui, side, slippage_tolerance=0.95):
    """
    Calculate the minimum output amount based on the input balance and current price from the pool.

    Args:
    - client: The client object for interacting with the blockchain.
    - pool_state: The state of the liquidity pool.
    - balance_ui: The input balance in user interface units (e.g., USDC, SOL).
    - slippage_tolerance: The percentage of slippage tolerance, default is 5%.

    Returns:
    - min_amount_out_atomic: The minimum output amount in atomic units.
    """

    # Retrieve the current price and token supplies from the pool state
    token_supply_amount = pool_state.vault_1_amount
    sol_supply_amount = pool_state.vault_0_amount

    # Scale the supply amounts according to their respective decimal places
    sol_scaled = int(sol_supply_amount) / 10**pool_state.mint_0_decimals
    token_scaled = int(token_supply_amount) / 10**pool_state.mint_1_decimals

    # Calculate the current price using scaled supplies
    price_now = token_scaled / sol_scaled
    print(f'actual price : {price_now}')


    if side == 'SELL':
        # Calculate the expected output amount in SOL (scaled)
        expected_output_amount = balance_ui / price_now

        # Apply the slippage tolerance
        min_amount_out_scaled = expected_output_amount * slippage_tolerance
        # Convert the minimum amount out back to atomic units
        min_amount_out_atomic = min_amount_out_scaled * 10**pool_state.mint_0_decimals  # Assuming SOL has mint_0_decimals
    else:
        # Calculate the expected output amount in SOL (scaled)
        expected_output_amount = balance_ui * price_now

        # Apply the slippage tolerance
        min_amount_out_scaled = expected_output_amount * slippage_tolerance
        # Convert the minimum amount out back to atomic units
        min_amount_out_atomic = min_amount_out_scaled * 10**pool_state.mint_1_decimals  # Assuming QUOTE has mint_1_decimals

    return min_amount_out_scaled, int(min_amount_out_atomic)
