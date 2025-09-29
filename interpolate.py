import pandas as pd

data=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv")

# data.loc[0,'pickup_year']=None
data.loc[1,'pickup_year']=None
data.loc[2,'pickup_year']=None
data.loc[0,'pickup_month']=None

print(data)

#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0              NaN           NaN           1  ...       11.65         69.99             1
#1              NaN           1.0           1  ...        8.00         54.30             1
#2              NaN           1.0           1  ...        0.00         37.80             2
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

data1 = data.interpolate()
print(data1)

#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0           2016.0           NaN           1  ...       11.65         69.99             1
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

data2=data.interpolate(method='linear',limit=2,axis=1)
#axis 1 will fill up data according to row. Similarly, axis=0 will go for columns.
print(data2)

#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0           2016.0        1008.5         1.0  ...       11.65         69.99           1.0
#1              NaN           1.0         1.0  ...        8.00         54.30           1.0
#2              NaN           1.0         1.0  ...        0.00         37.80           2.0
#3           2016.0           1.0         1.0  ...        5.46         32.76           1.0
#4           2016.0           1.0         1.0  ...        0.00         18.80           2.0
#...            ...           ...         ...  ...         ...           ...           ...
#89555       2016.0           6.0        30.0  ...        3.00         40.84           1.0
#89556       2016.0           6.0        30.0  ...        0.00         58.34           1.0
#89557       2016.0           6.0        30.0  ...        5.00         63.34           1.0
#89558       2016.0           6.0        30.0  ...        8.95         44.75           1.0
#89559       2016.0           6.0        30.0  ...        0.00         54.84           2.0
#
#[89560 rows x 15 columns]

data3=data.interpolate(limit_direction='backward',limit=1)
print(data3)

#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0           2016.0           1.0           1  ...       11.65         69.99             1
#1              NaN           1.0           1  ...        8.00         54.30             1
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

data4=data.interpolate(limit_direction='forward',limit=1)
print(data4)

#      pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0           2016.0           NaN           1  ...       11.65         69.99             1
#1           2016.0           1.0           1  ...        8.00         54.30             1
#2              NaN           1.0           1  ...        0.00         37.80             2
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