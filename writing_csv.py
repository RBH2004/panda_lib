import pandas as pd


data=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv")

print(data.index)

#RangeIndex(start=0, stop=89560, step=1)

print(data.columns)

#Index(['pickup_year', 'pickup_month', 'pickup_day', 'pickup_dayofweek',
#       'pickup_time', 'pickup_location_code', 'dropoff_location_code',
#       'trip_distance', 'trip_length', 'fare_amount', 'fees_amount',
#       'tolls_amount', 'tip_amount', 'total_amount', 'payment_type'],
#      dtype='object')

print(data.describe())


#       pickup_year  pickup_month    pickup_day  ...    tip_amount  total_amount  payment_type
#count      89560.0  89560.000000  89560.000000  ...  89560.000000  89560.000000  89560.000000     
#mean        2016.0      3.614471     15.693535  ...      5.814489     48.966662      1.290442     
#std            0.0      1.692354      8.694046  ...      4.832459     16.429253      0.476341     
#min         2016.0      1.000000      1.000000  ...      0.000000    -58.340000      1.000000     
#25%         2016.0      2.000000      8.000000  ...      0.000000     38.840000      1.000000     
#50%         2016.0      4.000000     16.000000  ...      6.470000     48.340000      1.000000     
#75%         2016.0      5.000000     23.000000  ...      9.460000     60.800000      2.000000     
#max         2016.0      6.000000     31.000000  ...    100.000000    834.840000      4.000000     
#
#[8 rows x 15 columns]

print(data.head())


#   pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0         2016             1           1  ...       11.65         69.99             1
#1         2016             1           1  ...        8.00         54.30             1
#2         2016             1           1  ...        0.00         37.80             2
#3         2016             1           1  ...        5.46         32.76             1
#4         2016             1           1  ...        0.00         18.80             2
#
#[5 rows x 15 columns]


print(data.head(2))

#   pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0         2016             1           1  ...       11.65         69.99             1
#1         2016             1           1  ...        8.00         54.30             1
#
#[2 rows x 15 columns]


print(data.tail(2))


#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#89558         2016             6          30  ...        8.95         44.75             1
#89559         2016             6          30  ...        0.00         54.84             2
#
#[2 rows x 15 columns]

print(data[:2])


#   pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0         2016             1           1  ...       11.65         69.99             1
#1         2016             1           1  ...        8.00         54.30             1
#
#[2 rows x 15 columns]


print(data[5:10])

#   pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#5         2016             1           1  ...       52.80        105.60             1
#6         2016             1           1  ...        6.45         32.25             1
#7         2016             1           1  ...        0.00         22.80             2
#8         2016             1           1  ...       10.00        131.38             1
#9         2016             1           1  ...        0.00         37.30             2
#
#[5 rows x 15 columns]


print(type(data))

#<class 'pandas.core.frame.DataFrame'>

print(data.index.array)

#<PandasArray>
#[    0,     1,     2,     3,     4,     5,     6,     7,     8,     9,
# ...
# 89550, 89551, 89552, 89553, 89554, 89555, 89556, 89557, 89558, 89559]
#Length: 89560, dtype: int64


print(data.to_numpy())

#<PandasArray>
#[    0,     1,     2,     3,     4,     5,     6,     7,     8,     9,
# ...
# 89550, 89551, 89552, 89553, 89554, 89555, 89556, 89557, 89558, 89559]
#Length: 89560, dtype: int64
#[[2.016e+03 1.000e+00 1.000e+00 ... 1.165e+01 6.999e+01 1.000e+00]
# [2.016e+03 1.000e+00 1.000e+00 ... 8.000e+00 5.430e+01 1.000e+00]
# [2.016e+03 1.000e+00 1.000e+00 ... 0.000e+00 3.780e+01 2.000e+00]
# ...
# [2.016e+03 6.000e+00 3.000e+01 ... 5.000e+00 6.334e+01 1.000e+00]
# [2.016e+03 6.000e+00 3.000e+01 ... 8.950e+00 4.475e+01 1.000e+00]
# [2.016e+03 6.000e+00 3.000e+01 ... 0.000e+00 5.484e+01 2.000e+00]]


print(data.sort_index(axis=0,ascending=False))

#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#89559         2016             6          30  ...        0.00         54.84             2
#89558         2016             6          30  ...        8.95         44.75             1
#89557         2016             6          30  ...        5.00         63.34             1
#89556         2016             6          30  ...        0.00         58.34             1
#89555         2016             6          30  ...        3.00         40.84             1
#...            ...           ...         ...  ...         ...           ...           ...
#4             2016             1           1  ...        0.00         18.80             2
#3             2016             1           1  ...        5.46         32.76             1
#2             2016             1           1  ...        0.00         37.80             2
#1             2016             1           1  ...        8.00         54.30             1
#0             2016             1           1  ...       11.65         69.99             1
#
#[89560 rows x 15 columns]


data.loc[0,'pickup_year']=2020
print(data)


#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0             2020             1           1  ...       11.65         69.99             1
#1             2016             1           1  ...        8.00         54.30             1
#2             2016             1           1  ...        0.00         37.80             2
#3             2016             1           1  ...        5.46         32.76             1
#4             2016             1           1  ...        0.00         18.80             2
#...            ...           ...         ...  ...         ...           ...           ...
#89555         2016             6          30  ...        3.00         40.84             1
#89556         2016             6          30  ...        0.00         58.34             1
#89557         2016             6          30  ...        5.00         63.34             1
#89558         2016             6          30  ...        8.95         44.75             1
#89559         2016             6          30  ...        0.00         54.84             2
#
#[89560 rows x 15 columns]


print(data.loc[[2,3],['pickup_year','pickup_month']])

#   pickup_year  pickup_month
#2         2016             1
#3         2016             1

data=data.drop('pickup_year',axis=1)

print(data)


#       pickup_month  pickup_day  pickup_dayofweek  ...  tip_amount  total_amount  payment_type
#0                 1           1                 5  ...       11.65         69.99             1    
#1                 1           1                 5  ...        8.00         54.30             1    
#2                 1           1                 5  ...        0.00         37.80             2    
#3                 1           1                 5  ...        5.46         32.76             1    
#4                 1           1                 5  ...        0.00         18.80             2    
#...             ...         ...               ...  ...         ...           ...           ...    
#89555             6          30                 4  ...        3.00         40.84             1    
#89556             6          30                 4  ...        0.00         58.34             1    
#89557             6          30                 4  ...        5.00         63.34             1    
#89558             6          30                 4  ...        8.95         44.75             1    
#89559             6          30                 4  ...        0.00         54.84             2    
#
#[89560 rows x 14 columns]