#stonk plot shows image but does not save any visuals

#  add the 5 day moving average +/5 5% to the pandas dataframe

def stock_plot(ticker, weeks_to_plot):
    import matplotlib.pyplot as plt
    import pandas_datareader as pdr 
    import pandas as pd
    from datetime import date, datetime, timezone, timedelta
    import json
    from PIL import Image
    
    #load the dictionary with coins, starting balance and USD to invest
    with open(ticker) as file:
        coin_dict = json.load(file)
    
    plt.close('all')

    for user, coins in coin_dict.items():
        for coin in coins:
            print (coin)
            print (user)

            tick = coin
            end_date = datetime.utcnow()
            start_date = datetime.utcnow()- timedelta(weeks = weeks_to_plot)
            ts = (pdr.get_data_yahoo(tick).loc[start_date: end_date])
            ts.rename(columns={'Adj Close':'Adj_Close'}, inplace=True)

            # #df = pd.DataFrame(stock_dataframe.Adj_Close, index = stock_dataframe.index)

            # ts.loc[start_date: end_date]


            ts['SMA_5'] = (ts.iloc[:,0].rolling(window=5).mean())


            ts['SMA_5_UL'] = (ts.iloc[:,5].rolling(window=5).mean()) * 1.05


            ts['SMA_5_LL'] = (ts.iloc[:,5].rolling(window=5).mean()) * .95


            #ts['sell'] = ts.iloc[:,0] > ts.iloc[:,1]

            #ts['buy'] = ts.iloc[:,0] < ts.iloc[:,2] 

            ts.loc[ts['Adj_Close'] > ts['SMA_5_UL'], 'Buy'] = ts['Adj_Close']

            ts.loc[ts['Adj_Close'] < ts['SMA_5_LL'], 'Sell'] = ts['Adj_Close']

            ts["Stock"] = tick


            
            # ts.plot()

            plt.plot( ts.Sell, 'go', ts.Buy, 'ro', ts.SMA_5, 'g-', ts.SMA_5_LL, 'c-', ts.SMA_5_UL, 'y-'
            , ts.Low, 'b--', ts.High, 'k--')

            plt.title(tick)
            plt.ylabel('Share Price')
            plt.legend(['Buy', 'Sell', 'Mean', 'LL', 'UL', 'daily_Low', 'daily_High'])
            #[ts.Adj_Close, ts.Sell, ts.Buy], 

            plt.savefig(tick+'plot.png', dpi=300, bbox_inches='tight')

            plt.show()


    return(ts)

#test
stock_plot("/home/yolindsay/stonks-code/trading_algos/coin_dict.json",5)


