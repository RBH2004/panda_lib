import pandas as pd


data=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv")



data.loc[0,'pickup_year']=None
data.loc[0,'pickup_month']=None

#print(data)

#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0              NaN           NaN           1  ...       11.65         69.99             1
#1           2016.0           1.0           1  ...        8.00         54.30             1
#2           2016.0           1.0           1  ...        0.00         37.80             2
#3           2016.0           1.0           1  ...        5.46         32.76             1
#4           2016.0           1.0           1  ...        0.00         18.80             2
#...            ...           ...         ...  ...         ...           ...           ...
#89555       2016.0           6.0          30  ...        3.00         40.84             1
#89556       2016.0           6.0          30  ...        0.00         58.34             1
#89557       2016.0           6.0          30  ...        5.00         63.34             1
#89558       2016.0           6.0          30  ...        8.95         44.75             1
#89559       2016.0           6.0          30  ...        0.00         54.84             2
#
#[89560 rows x 15 columns]


data2=data.dropna()
print(data2)



#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#1           2016.0           1.0           1  ...        8.00         54.30             1
#2           2016.0           1.0           1  ...        0.00         37.80             2
#3           2016.0           1.0           1  ...        5.46         32.76             1
#4           2016.0           1.0           1  ...        0.00         18.80             2
#5           2016.0           1.0           1  ...       52.80        105.60             1
#...            ...           ...         ...  ...         ...           ...           ...
#89555       2016.0           6.0          30  ...        3.00         40.84             1
#89556       2016.0           6.0          30  ...        0.00         58.34             1
#89557       2016.0           6.0          30  ...        5.00         63.34             1
#89558       2016.0           6.0          30  ...        8.95         44.75             1
#89559       2016.0           6.0          30  ...        0.00         54.84             2
#
#[89559 rows x 15 columns]


data3=data.dropna(axis=1) #removes columns with Nan data. similarly axis=0 removes rows with Nan data
print(data3)
#
#       pickup_day  pickup_dayofweek  pickup_time  ...  tip_amount  total_amount  payment_type
#0               1                 5            0  ...       11.65         69.99             1     
#1               1                 5            0  ...        8.00         54.30             1     
#2               1                 5            0  ...        0.00         37.80             2     
#3               1                 5            0  ...        5.46         32.76             1     
#4               1                 5            0  ...        0.00         18.80             2     
#...           ...               ...          ...  ...         ...           ...           ...     
#89555          30                 4            5  ...        3.00         40.84             1     
#89556          30                 4            5  ...        0.00         58.34             1     
#89557          30                 4            5  ...        5.00         63.34             1     
#89558          30                 4            5  ...        8.95         44.75             1     
#89559          30                 4            5  ...        0.00         54.84             2     
#
#[89560 rows x 13 columns]
#

data4=data.dropna(how='any') # removes the row with any the Nan values 
data5=data.dropna(how='all') # removes the row with all the Nan values

print(data)
data5=data.dropna(subset=['pickup_year'])
print(data5)

#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#1           2016.0           1.0           1  ...        8.00         54.30             1
#2           2016.0           1.0           1  ...        0.00         37.80             2
#3           2016.0           1.0           1  ...        5.46         32.76             1
#4           2016.0           1.0           1  ...        0.00         18.80             2
#5           2016.0           1.0           1  ...       52.80        105.60             1
#...            ...           ...         ...  ...         ...           ...           ...
#89555       2016.0           6.0          30  ...        3.00         40.84             1
#89556       2016.0           6.0          30  ...        0.00         58.34             1
#89557       2016.0           6.0          30  ...        5.00         63.34             1
#89558       2016.0           6.0          30  ...        8.95         44.75             1
#89559       2016.0           6.0          30  ...        0.00         54.84             2
#
#[89559 rows x 15 columns]


print(data)

#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0              NaN           NaN           1  ...       11.65         69.99             1
#1           2016.0           1.0           1  ...        8.00         54.30             1
#2           2016.0           1.0           1  ...        0.00         37.80             2
#3           2016.0           1.0           1  ...        5.46         32.76             1
#4           2016.0           1.0           1  ...        0.00         18.80             2
#...            ...           ...         ...  ...         ...           ...           ...
#89555       2016.0           6.0          30  ...        3.00         40.84             1
#89556       2016.0           6.0          30  ...        0.00         58.34             1
#89557       2016.0           6.0          30  ...        5.00         63.34             1
#89558       2016.0           6.0          30  ...        8.95         44.75             1
#89559       2016.0           6.0          30  ...        0.00         54.84             2
#
#[89560 rows x 15 columns]

data.dropna(inplace=True)
print(data)

#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#1           2016.0           1.0           1  ...        8.00         54.30             1
#2           2016.0           1.0           1  ...        0.00         37.80             2
#3           2016.0           1.0           1  ...        5.46         32.76             1
#4           2016.0           1.0           1  ...        0.00         18.80             2
#5           2016.0           1.0           1  ...       52.80        105.60             1
#...            ...           ...         ...  ...         ...           ...           ...
#89555       2016.0           6.0          30  ...        3.00         40.84             1
#89556       2016.0           6.0          30  ...        0.00         58.34             1
#89557       2016.0           6.0          30  ...        5.00         63.34             1
#89558       2016.0           6.0          30  ...        8.95         44.75             1
#89559       2016.0           6.0          30  ...        0.00         54.84             2
#
#[89559 rows x 15 columns]
data=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv")

data.loc[0,'pickup_year']=None
data.loc[0,'pickup_month']=None

data2=data.dropna(thresh=data.shape[1] - 1)   # removes rows with 2 Nan values
print(data2)

data3=data.fillna("CSE")
print(data3)

#      pickup_year pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0             CSE          CSE           1  ...       11.65         69.99             1
#1          2016.0          1.0           1  ...        8.00         54.30             1
#2          2016.0          1.0           1  ...        0.00         37.80             2
#3          2016.0          1.0           1  ...        5.46         32.76             1
#4          2016.0          1.0           1  ...        0.00         18.80             2
#...           ...          ...         ...  ...         ...           ...           ...
#89555      2016.0          6.0          30  ...        3.00         40.84             1
#89556      2016.0          6.0          30  ...        0.00         58.34             1
#89557      2016.0          6.0          30  ...        5.00         63.34             1
#89558      2016.0          6.0          30  ...        8.95         44.75             1
#89559      2016.0          6.0          30  ...        0.00         54.84             2
#
#[89560 rows x 15 columns]

data4=data.fillna({'pickup_year':'eee','pickup_month':'cse'})
print(data4)

#      pickup_year pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0             eee          cse           1  ...       11.65         69.99             1
#1          2016.0          1.0           1  ...        8.00         54.30             1
#2          2016.0          1.0           1  ...        0.00         37.80             2
#3          2016.0          1.0           1  ...        5.46         32.76             1
#4          2016.0          1.0           1  ...        0.00         18.80             2
#...           ...          ...         ...  ...         ...           ...           ...
#89555      2016.0          6.0          30  ...        3.00         40.84             1
#89556      2016.0          6.0          30  ...        0.00         58.34             1
#89557      2016.0          6.0          30  ...        5.00         63.34             1
#89558      2016.0          6.0          30  ...        8.95         44.75             1
#89559      2016.0          6.0          30  ...        0.00         54.84             2
#
#[89560 rows x 15 columns]

data5=data.fillna(method='bfill') #fills the Nan values with data from the back row
print(data5)

#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0           2016.0           1.0           1  ...       11.65         69.99             1
#1           2016.0           1.0           1  ...        8.00         54.30             1
#2           2016.0           1.0           1  ...        0.00         37.80             2
#3           2016.0           1.0           1  ...        5.46         32.76             1
#4           2016.0           1.0           1  ...        0.00         18.80             2
#...            ...           ...         ...  ...         ...           ...           ...
#89555       2016.0           6.0          30  ...        3.00         40.84             1
#89556       2016.0           6.0          30  ...        0.00         58.34             1
#89557       2016.0           6.0          30  ...        5.00         63.34             1
#89558       2016.0           6.0          30  ...        8.95         44.75             1
#89559       2016.0           6.0          30  ...        0.00         54.84             2
#
#[89560 rows x 15 columns