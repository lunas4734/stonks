#trading algo execute

#produce a trigger that sends an email if the stock dips below the mean

#list of stocks to watch=done
#user belonging to stocks=done
#create the coin tuple that has the date and stock price=done
#an email that can be sent= done
# a graph attachement in an email =done
# a trigger that sends an email to buy or sell
#trigger needs to look for daily volitility
#create a csv file that stores the daily volititliy for each stock

#a trigger to buy or a trigger to sell, no knowledge of holdings needed



import matplotlib.pyplot as plt
import pandas_datareader as pdr 
import pandas as pd
from datetime import date, datetime, timezone, timedelta

plt.close('all')

tick = 'F'
end_date = datetime.utcnow()
start_date = datetime.utcnow()- timedelta(52)
stock_dataframe= (pdr.get_data_yahoo(tick))
print(stock_dataframe)
#stock_dataframe.rename(columns={'Adj Close':'Adj_Close'}, inplace=True)