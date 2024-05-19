from solders.pubkey import Pubkey
from utils.layout import POOL_STATE_LAYOUT, AMM_CONFIG_LAYOUT, OBSERVATION_STATE

# Enum for PoolStatusBitIndex
class PoolStatusBitIndex:
    Deposit = 0
    Withdraw = 1
    Swap = 2

# Enum for PoolStatusBitFlag
class PoolStatusBitFlag:
    Enable = 0
    Disable = 1

# Constants
POOL_SEED = "pool"
POOL_LP_MINT_SEED = "pool_lp_mint"
POOL_VAULT_SEED = "pool_vault"
Q32 = (2 ** 32)

class PoolState:
    """
    PoolState class represents the state of a liquidity pool in a decentralized exchange (DEX) environment. 
    It encapsulates the details of the pool's configuration, token vaults, LP mint, fees, and observations. 
    This class provides methods to fetch and parse data from the blockchain, manage pool statuses, and calculate 
    relevant metrics such as token prices.

    Attributes:
        client (object): Client object used for blockchain interaction.
        pool_state (Pubkey): Public key representing the pool state address.
        data (dict): Dictionary containing parsed pool state data.
        amm_config (Pubkey): Public key of the AMM configuration.
        pool_creator (Pubkey): Public key of the pool creator.
        token_0_vault (Pubkey): Public key of the vault for token 0.
        token_1_vault (Pubkey): Public key of the vault for token 1.
        lp_mint (Pubkey): Public key of the LP mint.
        token_0_mint (Pubkey): Public key of the mint for token 0.
        token_1_mint (Pubkey): Public key of the mint for token 1.
        token_0_program (Pubkey): Public key of the token 0 program.
        token_1_program (Pubkey): Public key of the token 1 program.
        observation_key (Pubkey): Public key of the observation key.
        auth_bump (int): Authentication bump.
        status (int): Status of the pool.
        lp_mint_decimals (int): Decimals of the LP mint.
        mint_0_decimals (int): Decimals of the mint for token 0.
        mint_1_decimals (int): Decimals of the mint for token 1.
        lp_supply (int): Supply of LP tokens.
        protocol_fees_token_0 (int): Protocol fees for token 0.
        protocol_fees_token_1 (int): Protocol fees for token 1.
        fund_fees_token_0 (int): Fund fees for token 0.
        fund_fees_token_1 (int): Fund fees for token 1.
        open_time (int): Open time of the pool.
        amm_cfg (dict): AMM configuration data.
        vault_amount (tuple): Amount of tokens in the vaults.
        vault_amount_without_fee (tuple): Vault amounts without fees.
        observations (dict): Observations data.
    """

    def __init__(self, pool_state_address, client):
        self.client = client
        self.pool_state = Pubkey.from_string(pool_state_address)
        self.data = self.get_pool_state()
        
        # Store relevant pool data from the fetched state
        self.amm_config = self.data['amm_config']
        self.pool_creator = self.data['pool_creator']
        self.token_0_vault = self.data['token_0_vault']
        self.token_1_vault = self.data['token_1_vault']
        self.lp_mint = self.data['lp_mint']
        self.token_0_mint = self.data['token_0_mint']
        self.token_1_mint = self.data['token_1_mint']
        self.token_0_program = self.data['token_0_program']
        self.token_1_program = self.data['token_1_program']
        self.observation_key = self.data['observation_key']
        self.auth_bump = self.data['auth_bump']
        self.status = self.data['status']
        self.lp_mint_decimals = self.data['lp_mint_decimals']
        self.mint_0_decimals = self.data['mint_0_decimals']
        self.mint_1_decimals = self.data['mint_1_decimals']
        self.lp_supply = self.data['lp_supply']
        self.protocol_fees_token_0 = self.data['protocol_fees_token_0']
        self.protocol_fees_token_1 = self.data['protocol_fees_token_1']
        self.fund_fees_token_0 = self.data['fund_fees_token_0']
        self.fund_fees_token_1 = self.data['fund_fees_token_1']
        self.open_time = self.data['open_time']
        
        # Initialize AMM CFG
        self.amm_cfg = self.get_amm_cfg()

        #Get oracle price
        self.observations = self.get_observations()

        #Calculate vault amout and vault amount without fees
        self.vault_amout = self.get_vault_amount()
        self.vault_amount_without_fees = self.vault_amount_without_fee()
        

    def get_vault_amount(self):
        # Fetch token amounts from vaults
        resp_token_amount_0 = self.client.get_account_info_json_parsed(
            self.token_0_vault, commitment='confirmed').value.data
        self.vault_0_amount = int(resp_token_amount_0.parsed['info']['tokenAmount']['amount'])

        resp_token_amount_1 = self.client.get_account_info_json_parsed(
            self.token_1_vault, commitment='confirmed').value.data
        self.vault_1_amount = int(resp_token_amount_1.parsed['info']['tokenAmount']['amount'])

        return self.vault_0_amount, self.vault_1_amount

    def get_pool_state(self):
        # Fetch and parse pool state data
        pool_state_data = self.client.get_account_info_json_parsed(self.pool_state, commitment='confirmed').value.data
        parsed_data = POOL_STATE_LAYOUT.parse(pool_state_data)

        data = {
            "amm_config": Pubkey.from_bytes(parsed_data.amm_config),
            "pool_creator": Pubkey.from_bytes(parsed_data.pool_creator),
            "token_0_vault": Pubkey.from_bytes(parsed_data.token_0_vault),
            "token_1_vault": Pubkey.from_bytes(parsed_data.token_1_vault),
            "lp_mint": Pubkey.from_bytes(parsed_data.lp_mint),
            "token_0_mint": Pubkey.from_bytes(parsed_data.token_0_mint),
            "token_1_mint": Pubkey.from_bytes(parsed_data.token_1_mint),
            "token_0_program": Pubkey.from_bytes(parsed_data.token_0_program),
            "token_1_program": Pubkey.from_bytes(parsed_data.token_1_program),
            "observation_key": Pubkey.from_bytes(parsed_data.observation_key),
            "auth_bump": parsed_data.auth_bump,
            "status": parsed_data.status,
            "lp_mint_decimals": parsed_data.lp_mint_decimals,
            "mint_0_decimals": parsed_data.mint_0_decimals,
            "mint_1_decimals": parsed_data.mint_1_decimals,
            "lp_supply": parsed_data.lp_supply,
            "protocol_fees_token_0": parsed_data.protocol_fees_token_0,
            "protocol_fees_token_1": parsed_data.protocol_fees_token_1,
            "fund_fees_token_0": parsed_data.fund_fees_token_0,
            "fund_fees_token_1": parsed_data.fund_fees_token_1,
            "open_time": parsed_data.open_time,
        }
        return data

    def get_observations(self):
        # Fetch and parse observation data
        observation_data = self.client.get_account_info_json_parsed(self.observation_key, commitment='confirmed').value.data
        parsed_data = OBSERVATION_STATE.parse(observation_data)
        
        data = {
            "initialized": parsed_data.initialized,
            "observation_index": parsed_data.observationIndex,
            "pool_id": Pubkey.from_bytes(parsed_data.poolId),
            "observations": []
        }
        print(parsed_data.observations)
        # Convert observations to dictionary format
        for obs in parsed_data.observations:
            obs_dict = {
                "block_timestamp": obs.block_timestamp,
                "cumulative_token_0_price_x32": obs.cumulative_token_0_price_x32,
                "cumulative_token_1_price_x32": obs.cumulative_token_1_price_x32
            }
            data["observations"].append(obs_dict)

        return data

    def get_amm_cfg(self):
        # Fetch and parse AMM configuration data
        amm_data = self.client.get_account_info_json_parsed(self.amm_config, commitment='confirmed').value.data
        amm_data_decoded = AMM_CONFIG_LAYOUT.parse(amm_data)

        data = {
            "bump": amm_data_decoded.bump,
            "disable_create_pool": amm_data_decoded.disable_create_pool,
            "index": amm_data_decoded.index,
            "trade_fee_rate": amm_data_decoded.trade_fee_rate,
            "protocol_fee_rate": amm_data_decoded.protocol_fee_rate,
            "fund_fee_rate": amm_data_decoded.fund_fee_rate,
            "create_pool_fee": amm_data_decoded.create_pool_fee,
            "protocol_owner": Pubkey.from_bytes(amm_data_decoded.protocol_owner),
            "fund_owner": Pubkey.from_bytes(amm_data_decoded.fund_owner),
        }
        return data

    def vault_amount_without_fee(self):
        # Calculate vault amounts without fees
        return (
            self.vault_0_amount - (self.protocol_fees_token_0 + self.fund_fees_token_0),
            self.vault_1_amount - (self.protocol_fees_token_1 + self.fund_fees_token_1)
        )

    def token_price_x32(self):
        # Calculate token prices
        token_0_amount, token_1_amount = self.vault_amount_without_fee()
        return (
            (token_1_amount * Q32) // token_0_amount,
            (token_0_amount * Q32) // token_1_amount
        )
