
import pandas_datareader as pdr 
import pandas as pd
from datetime import date, datetime, timezone
import numpy as np

#create my personal datafram from pandas data reader    
tick = 'F'
stock_dataframe= (pdr.get_data_yahoo(tick))

print(stock_dataframe)

#tutorial dataframe


#create a list of date ranges
d = pd.date_range('20200301', periods = 10)

print(d)

#create a data frame with random numbers, the index being the date range and colums from a list
df = pd.DataFrame(np.random.randn(10,4), index=d, columns=['A', 'B', 'C', 'D'])

print(df)

#create a second dataframe from a dictionary
df1 = pd.DataFrame({'A': [1,2,3,4],
                    'B':pd.Timestamp('20200301'),
                    'C': pd.Series(1, index = list(range(4)), dtype='float32'),
                    'D':np.array([5]*4, dtype='int32'),
                    'E': pd.Categorical(['true', 'false', 'true', 'false']),
                    'F': 'Edureka'
})

print(df1)

print(df1.dtypes)

print(df.tail())
print(df1.head())

print(df.index)
print(df.columns)

#transfer a float dataframe to numpy
df.to_numpy
print(df)

#show statistics on the dataframe
print(df.describe())

#sort the dataframe
print('sorted by index')
print(df.sort_index(axis=1, ascending= False))
print('sorted by column C')
print(df.sort_values(by ='C'))

#slect locations
#select column
print('select column')
print(df['C'])


#select rows
print('select rows')
print(df[0:6])


#select rows
print('select rows')
print(df.loc[d[0]])


print('select a range and columns')
print(df.loc['20200301':'20200306' , ['A', 'D']])

print('select a location in the index and columns')
print(df.loc['20200301', ['A', 'D']])

print('select a location by position and columns')
print(df.loc[d[1], ['A', 'D']])

print('select a coordinate')
print(df.at[d[1], 'D'])

print('Selecting integer location')
print(df.iloc[3])

print('Selecting integer location and pivot')
print(df.iloc[[3]])

print('select integer location range of rows and columns')
print(df.iloc[3:5])

print('select values that are true for an expression')
print(df[df['A'] > 0])




#handling missing data

#create a new dataframe from df and add a new column E
df2 = df.reindex(index=d[0:4], columns = list(df.columns) + ['E'])

print('newly added column E')
print(df2)

#add values to new column
print('add values to E')
df2.loc[d[0]:d[1], 'E'] =1

print(df2)

#find the null values
print('finding nulls')
print(df2.isnull())

#count the null values
print('count nulls')
print(df2.isnull().count())

#drop nulls
print('drop null values')
print(df2.dropna())

#replace NA values
print('fill na values')
print(df2.fillna(value = 2))

#find the NA values
print(pd.isna(df2))



#pandas oporations

print('dataframe mean for all columns')
print(df.mean())

print('dataframe mean for first row')
print(df.mean(1))

#create a dataframe with a nan value with an axis shifted by two
s= pd.Series([1,2,3,np.nan, 4,5,6,7,8,9], index=d).shift(2)

print('new dataframe s with nan value')
print(s)

#apply one series to a dataframe
print('new series s subsituted in df')
print(df.sub(s, axis='index'))

#cumulative sum
print('cumulative sum of all columns')
print(df.apply(np.cumsum))

print('lambda functions, min minus max for all columns (range)')
print(df.apply(lambda x: x.max() - x.min()))

#histogram
print('count of each value in series s as histogram')
print(s.value_counts())

#create a new string
s = pd.Series(['edureka', 'python', 'jupyter', np.nan, 'football', 'world'])
print('upper case of the string s')
print(s.str.upper())

#merging
df = pd.DataFrame(np.random.rand(10, 4))

print(df)

df2= [df[:3], df[3:7], df[7:]]
print(df2)

print(pd.concat(df2))

left = pd.DataFrame({'A': [1,2],
    'B': [3,4]
    
})

right = pd.DataFrame({'A': [3,2],
    'D': [4,5]
    
})

print (left)
print(right)
print(pd.merge(left, right, on = 'A'))
#this is a join function, like sql

#grouping like in sql
print(df.groupby(2).sum())

print(df.groupby([2,3]).sum())


#merge grop and reshape data

my_tuple = list(zip(*[[1,2,3,4,5,17,18,19], [11,12,13,6,7,8,9,10]]))

index = pd.MultiIndex.from_tuples(my_tuple, names = ['First', 'Second'])

df = pd.DataFrame(np.random.rand(8,2,), index = index, columns = ['A', 'B'])

df2 = df[:4]

print(df2)

a = df2.stack()

print(a)

print(a.unstack())

df = pd.DataFrame({'A': ['a', 'b', 'c', 'd'] * 3,
                    'B': ['A', 'B', 'C'] * 4,
                    'C' : ['P','P', 'P', 'Q', 'Q', 'Q'] *2,
                    'D': np.random.randn(12),
                    'E': np.random.randn(12)
})

print(df)

print(pd.pivot_table(df, values = 'D', index= ['A', 'B'], columns = ['C'] ))


#time series and catagoricals

dates = pd.date_range('3/3/2020 00:00', periods = 100, freq = 'S')

print(dates)

ts = pd.Series(np.random.randint(0, 500, len(dates)), dates)

print (ts)

print(ts.resample('5min').sum)

dates = pd.date_range('3/3/2020 00:00', periods = 5, freq = 'S')

ts = pd.Series(np.random.randn(len(dates)), dates)

print(ts)

ts_utc = ts.tz_localize('UTC')

print(ts_utc)

ts_utc.tz_convert('US/Eastern')

dates = pd.date_range('3/3/2020', periods = 5, freq = 'M')

ts = pd.Series(np.random.randn(len(dates)), dates)

print(ts)

ps = ts.to_period()

print(ps)

ps.to_timestamp()

print(ps)

df = pd.DataFrame({'id': [1,2,3,4,5,6],
                    "grade": ['a', 'b', 'c', 'b', 'a', 'f']
})

print(df)

df['Grade'] = df['grade'].astype("category")
print(df["Grade"])

df["Grade"].cat.categories = ["good", "very bad", "very good", "excelent"]

print(df['Grade'].cat.categories)

df['Grade'] = df["Grade"].cat.set_categories(["very good", "bad", "very bad", "good","medium"])

print(df["Grade"])



