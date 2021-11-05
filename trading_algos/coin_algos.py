#create coin list json files
from JSON_funcs import save_json

coins = {
    "lindsay": ["VTI", "UAL", "GME", "AMC", "RBLX", "F", 'DIS', 'AMZN', 'AAPL'] #, "BTC-USD"
    , "Ryan": ['GME']
    
}


save_json(coins, "/home/yolindsay/stonks-code/trading_algos/", 'coin_dict')


#coin/stock web data to tuple
def data_to_tuple (ticker, start):
    import pandas_datareader as pdr 
    import pandas as pdf
    from datetime import date, datetime, timezone
    
    tick = ticker
    stock_dataframe= (pdr.get_data_yahoo(tick))
    stock_dataframe.rename(columns={'Adj Close':'Adj_Close'}, inplace=True)
    coin = {}
    start_date = start
    end_date = (datetime.utcnow()).strftime('%m-%d-%Y')
    
    index = stock_dataframe.loc[start_date:end_date].index.tolist() 
    index  = [line.strftime('%d-%m-%Y') for line in stock_dataframe.loc[start_date:end_date].index.tolist()]
    price  = [round(float(line), 2) for line in stock_dataframe.loc[start_date:end_date].Adj_Close.tolist()]
    
    coin["dayprice"] = []
    for i in range(0, len(index)):
        merged = (index[i], price[i]) 
        coin["dayprice"].append(merged)
    return (coin)
    
# # test here      
# print(data_to_tuple('VTI', '2020-02-01'))
