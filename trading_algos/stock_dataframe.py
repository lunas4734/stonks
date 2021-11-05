#stonk plot shows image but does not save any visuals

# I would like to add the 5 day moving average +/5 5% to the pandas dataframe

#stock dataframe creation

def stock_trend(ticker, weeks_to_trend):
    import pandas_datareader as pdr 
    import pandas as pd
    from datetime import date, datetime, timezone, timedelta

    tick = ticker
    end_date = datetime.utcnow()
    start_date = datetime.utcnow()- timedelta(weeks = weeks_to_trend)
    stock_dataframe= (pdr.get_data_yahoo(tick))
    stock_dataframe.rename(columns={'Adj Close':'Adj_Close'}, inplace=True)


    df = pd.DataFrame(stock_dataframe.Adj_Close, index = stock_dataframe.index)

    ts = df.loc[start_date: end_date]

    print(ts)

    #ts['pandas_SMA_5'] = ts.iloc[:,0].rolling(window=5).mean()


    ts['SMA_5_UL'] = (ts.iloc[:,0].rolling(window=5).mean()) * 1.05

    print(ts)

    ts['SMA_5_LL'] = (ts.iloc[:,0].rolling(window=5).mean()) * .95

    print(ts)

    #ts['sell'] = ts.iloc[:,0] > ts.iloc[:,1]

    #ts['buy'] = ts.iloc[:,0] < ts.iloc[:,2] 

    ts.loc[ts['Adj_Close'] > ts['SMA_5_UL'], 'Sell'] = ts['Adj_Close']

    ts.loc[ts['Adj_Close'] < ts['SMA_5_LL'], 'Buy'] = ts['Adj_Close']

    print(ts)

    return(ts, ticker)

#test
stock_trend('AMC', 52)