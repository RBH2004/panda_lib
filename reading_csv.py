import pandas as pd

data=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv")
print(data)

row_one=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv",nrows=1)
print(row_one)

#0         2016             1           1  ...       11.65         69.99             1
#
#[1 rows x 15 columns]

get_column=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv",usecols=['pickup_year'])
print(get_column)
get_column_2=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv",usecols=[0,1])
print(get_column_2)


#[1 rows x 15 columns]
#       pickup_year
#0             2016
#1             2016
#2             2016
#3             2016
#4             2016
#...            ...
#89555         2016
#89556         2016
#89557         2016
#89558         2016
#89559         2016