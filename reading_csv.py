import pandas as pd

data=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv")
print(data)

row_one=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv",nrows=1)
print(row_one)

#0         2016             1           1  ...       11.65         69.99             1
#
#[1 rows x 15 columns]

get_column