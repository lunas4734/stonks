#This file holds the trading strategy function and the function calls for each strategy.



from datetime import datetime, timezone

#Define main strategy Function
#Inputs are the tuple of prices(date, price) from the csv, 
#   ticker name or coin name, buy_strategy function, 
#   sell_strategy function, the strategy name to display, 
#   the beginig coin balance and the USDs set aside to purchase for each coin.

def tradingStrategy(prices,
    ticker,
    buy_strategy, 
    sell_strategy, 
    strategy_name
    #begining_coin_balance,
    #USDs_to_invest
):
    print("\n")
    print("-------------------------")
    print(ticker, strategy_name, " Strategy Output")
    i = 0
    #rate USD/coin
    buy = 0
    #define the current date for coin day comparison
    now = (datetime.utcnow()).strftime('%m-%d-%Y')
    #set buy date varaibles
    buy_date = (1-1-2019)
    #set sell date variabbles
    sell_date = (1-1-2019)
    #set action needed today variable
    take_action = 'do nothing'
    #begin processing csvs through function.
    for price in prices:
        #count the numer of rounds, start at the 5th record after calculating 5d moving avereage
        if i >= 5:
            #create 5 day moving average using the previous 5 records, positino 1 of tuple
            moving_average = (prices[i-1][1] + prices[i-2][1] + prices[i-3][1] + prices[i-4][1] + prices[i-5][1])/5
            #call the strategy function variales
            if buy_strategy(float(price[1]), moving_average):
                buy = price[1]
                print("buying at: ", price[1],"on", price[0])
                buy_date = price[0]
            elif sell_strategy(float(price[1]), moving_average, price[0], now):
                sell = price[1]
                print ("selling at: ", price[1], "on", price[0])
                sell_date = price[0]
            else:
                pass
        #update the number of rounds counter
        i = i + 1
    print("-----------------------------")
    print(ticker, strategy_name)
    if buy_date == now:
        print("BUY TODAY on : ", buy_date)
        take_action = "BUY TODAY"
    else:
        print("last suggested buy:", buy_date)
    if sell_date == now:
        print("SELL TODAY on: ", sell_date)
        take_action = "SELL TODAY"
    else: 
        print("last sell:", sell_date)
    return take_action, now, sell_date

###______function calls for each strategy

#Define mean reversion function.
# Mean reversion (buy low, sell high)looks for a rise 5% above the mean before selling,
#    and a dip 5% below the mean before buying. 


#set the buy sell functions for Mean Reversion strategy
def MR_buy(todays_price, moving_average):
    return (todays_price < (moving_average * .95))

def MR_sell(todays_price, moving_average, day, now):
    return (todays_price > (moving_average * 1.05) )
    
#Create a tuple for the strategy buy, sell functions and the name
mean_reversion = [MR_buy, MR_sell, 'MeanReversionStrategy']


#define simple moving average function
#simple moving average looks for a ris above the mean as an indicator to buy,
#    and a dip below the mean as an indicator to sell.  

#Set the buy sell functions for simple moving average
def SMA_buy(todays_price, moving_average):
    return (todays_price > moving_average)
    
def SMA_sell(todays_price, moving_average, day, now):
    return (todays_price < moving_average)


#Create a tuple for the strategy buy, sell functions and the name
simple_moving_average = [SMA_buy, SMA_sell, "SimpleMovingAverage"]


#define diamond hands function
#diamond hands function buys at the first dip below 5%
#set the buy sell functions for diamond hands (buy the dip and hold)
#   and it holds until the value of the coin reaches 1 million 
#   or the date is today and you must liquidate.
def DH_buy(todays_price, moving_average):
    return (todays_price < (moving_average * 0.95) )

def DH_sell(todays_price, moving_average, day, now):
    return ( day == now )

#Create a tuple for the strategy buy, sell functions and the name
diamond_hands = (DH_buy, DH_sell, "DiamondHands")



