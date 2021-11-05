#this file executes the trading results

#Import functions from coin lists, json saving and trading algos
from coin_algos import data_to_tuple #coin_append_fun, coin_load_func, csv_to_tuple,
from JSON_funcs import save_json
import json
from trading_algorithms import  tradingStrategy, mean_reversion, simple_moving_average, diamond_hands

#load the dictionary with coins, starting balance and USD to invest
with open("/home/yolindsay/stonks-code/trading_algos/coin_dict.json") as file:
    coin_dict = json.load(file)

#from coin disctionary, create list of coins to update csv files
lindsays_coins = []
for coins, values in coin_dict.items():
    lindsays_coins.append(coins)


#create strategy dictionary of all the strategy functions 
#   so that name can be labeled independent of funciton
strategies = {
    "MeanReversionStrategy": mean_reversion,
    "SimpleMovingAverage": simple_moving_average,
    #"DiamondHands": diamond_hands
}

#create dictionary for result storage
results = {}

for strategyName, function in strategies.items():
    per_strategy = {}
    for user, stocks in coin_dict.items():
        for coinage in stocks:
            coin_rate = data_to_tuple(coinage, '2021-02-01')
            per_strategy[coinage] = tradingStrategy(coin_rate["dayprice"], coinage, *function)


    #save function output to results dictionary
    results[strategyName] = per_strategy

#save dictionary to JSON        
save_json(results, "/home/yolindsay/stonks-code/trading_algos", "finalResults")







