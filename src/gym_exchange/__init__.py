"""gym_exchange: implementations of gym_exchange and reward learning algorithms."""

# from importlib import metadata

# try:
#     __version__ = metadata.version("gym_exchange")
# except metadata.PackageNotFoundError:  # pragma: no cover
#     # package is not installed
#     pass




# =================================================================

from gym.envs.registration import register

class Config:
    # --------------- 00 Data ---------------
    # ············· 00.01 Adapter ············
    raw_price_level = 10
    # raw_horizon = 2048
    # raw_horizon = 3700
    raw_horizon = 4096
    type5_id_bid = 30000000  # caution about the volumn for valid numbers
    type5_id_ask = 40000000  # caution about the volumn for valid numbers
    # ············· 00.02 Source ············
    exchange_data_source = "raw_encoder"
    # exchange_data_source = "encoder"


    # --------------- 01 Basic ---------------
    tick_size = 100 #(s hould be divided by 10000 to be converted to currency)
    price_level = 10
    lobster_scaling = 10000 # Dollar price times 10000 (i.e., A stock price of $91.14 is given by 911400)
    # max_horizon = 4096
    # max_horizon = 2048
    max_horizon = raw_horizon
    # max_horizon = 1600
    # max_horizon = 800
    # max_horizon = 600


    # --------------- 02 Reward ---------------
    low_dimension_penalty_parameter = 1 # todo not sure
    cost_parameter = 5e-6 # from paper.p29 : https://epubs.siam.org/doi/epdf/10.1137/20M1382386
    phi_prime = 5e-6 # from paper.p29 : https://epubs.siam.org/doi/epdf/10.1137/20M1382386

    # --------------- 03 Task ---------------
    num2liquidate = 200 # 1 min
    '''num2liquidate = 2000 # 10 min, 200 # 1 min, 100 # 1/2 min'''

    # --------------- 04 Action ---------------
    timeout = 10

    # --------------- 05 ActionWrapper --------
    trade_id_generator = 80000000
    order_id_generator = 88000000

    # --------------- 06 Space ---------------
    max_action = 300
    max_quantity = 3000 # TODO is it the same function with max_action?
    max_price = 35000000 # upper bound
    min_price = 30000000 # lower bound
    min_quantity = 0
    scaling = 30000000
    min_num_left = 0
    max_num_left = num2liquidate
    min_step_left= 0
    max_step_left = max_horizon
    state_dim_1 = 2 # price, quantity
    state_dim_2 = price_level # equals 10

    # --------------- 07 Observation ---------------
    lock_back_window = 60 # all the states after 60 actions was conducted
    # num_ticks =  lock_back_window * skip # 1min, num_ticks
    '''num_ticks = 1200 # 1min, num_ticks'''

    # --------------- 08 Output ---------------
    out_path = '/Users/kang/AlphaTrade/gym_exchange/outputs/'

    # --------------- 09 Random ---------------
    seed = 1234



register(
    id = "GymExchange-v1",
    # path to the class for creating the env
    # Note: entry_point also accept a class as input (and not only a string)
    entry_point="gym_exchange.trading_environments.stock_env:StockEnv", # TODO
    kwargs={'Flow': True},
    # Max number of steps per episode, using a `TimeLimitWrapper`
    max_episode_steps=Config.max_horizon,
    )
