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

get_column_2=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv",usecols=[0,1])
print(get_column_2)




#[89560 rows x 1 columns]
#       pickup_year  pickup_month
#0             2016             1
#1             2016             1
#2             2016             1
#3             2016             1
#4             2016             1
#...            ...           ...
#89555         2016             6
#89556         2016             6
#89557         2016             6
#89558         2016             6
#89559         2016             6


skip_row=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv",skiprows=[0,3])
print(skip_row)

#       2016  1  1.1  5  0  2  4  21.00  2037  52.00  0.80  5.54  11.65   69.99  1.2
#0      2016  1    1  5  0  2  1  16.29  1520   45.0   1.3  0.00   8.00   54.30    1
#1      2016  1    1  5  0  2  6   8.70  1210   26.0   1.3  0.00   5.46   32.76    1
#2      2016  1    1  5  0  2  6   5.56   759   17.5   1.3  0.00   0.00   18.80    2
#3      2016  1    1  5  0  4  2  21.45  2004   52.0   0.8  0.00  52.80  105.60    1
#4      2016  1    1  5  0  2  6   8.45   927   24.5   1.3  0.00   6.45   32.25    1
#...     ... ..  ... .. .. .. ..    ...   ...    ...   ...   ...    ...     ...  ...
#89553  2016  6   30  4  5  3  4   9.50  1989   31.0   1.3  5.54   3.00   40.84    1
#89554  2016  6   30  4  5  2  4  19.80  2368   52.0   0.8  5.54   0.00   58.34    1
#89555  2016  6   30  4  5  2  4  17.48  2822   52.0   0.8  5.54   5.00   63.34    1
#89556  2016  6   30  4  5  2  6  12.76  1083   34.5   1.3  0.00   8.95   44.75    1
#89557  2016  6   30  4  5  2  0  17.54  1711   48.0   1.3  5.54   0.00   54.84    2            2

index_col=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv",index_col=0)
print(index_col)


#             pickup_month  pickup_day  pickup_dayofweek  ...  tip_amount  total_amount  payment_type
#pickup_year                                              ...                                      
#
#2016                    1           1                 5  ...       11.65         69.99            
# 1
#2016                    1           1                 5  ...        8.00         54.30            
# 1
#2016                    1           1                 5  ...        0.00         37.80             2
#2016                    1           1                 5  ...        5.46         32.76             1
#2016                    1           1                 5  ...        0.00         18.80             2
#...                   ...         ...               ...  ...         ...           ...           ...
#2016                    6          30                 4  ...        3.00         40.84             1
#2016                    6          30                 4  ...        0.00         58.34             1
#2016                    6          30                 4  ...        5.00         63.34             1
#2016                    6          30                 4  ...        8.95         44.75             1
#2016                    6          30                 4  ...        0.00         54.84             2
#
#[89560 rows x 14 columns]

header_build=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv",header=2)
print(header_build)
#
#       2016  1  1.1  5  0  2  1.2  16.29  1520  45.00  1.30  0.00   8.00   54.30  1.3
#0      2016  1    1  5  0  2    6  12.70  1462   36.5   1.3  0.00   0.00   37.80    2
#1      2016  1    1  5  0  2    6   8.70  1210   26.0   1.3  0.00   5.46   32.76    1
#2      2016  1    1  5  0  2    6   5.56   759   17.5   1.3  0.00   0.00   18.80    2
#3      2016  1    1  5  0  4    2  21.45  2004   52.0   0.8  0.00  52.80  105.60    1
#4      2016  1    1  5  0  2    6   8.45   927   24.5   1.3  0.00   6.45   32.25    1
#...     ... ..  ... .. .. ..  ...    ...   ...    ...   ...   ...    ...     ...  ...
#89553  2016  6   30  4  5  3    4   9.50  1989   31.0   1.3  5.54   3.00   40.84    1
#89554  2016  6   30  4  5  2    4  19.80  2368   52.0   0.8  5.54   0.00   58.34    1
#89555  2016  6   30  4  5  2    4  17.48  2822   52.0   0.8  5.54   5.00   63.34    1
#89556  2016  6   30  4  5  2    6  12.76  1083   34.5   1.3  0.00   8.95   44.75    1
#89557  2016  6   30  4  5  2    0  17.54  1711   48.0   1.3  5.54   0.00   54.84    2
#
#[89558 rows x 15 columns]


name_heading=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv",names=['Unga bunga','nigga'])
print(name_heading)


#                                                                                                  
#                                                                                       Unga bunga         nigga
#pickup_year pickup_month pickup_day pickup_dayofweek pickup_time pickup_location_code dropoff_location_code trip_distance trip_length fare_amount fees_amount tolls_amount tip_amount  total_amount  payment_type
#2016        1            1          5                0           2                    4           
#          21.00         2037        52.00       0.80        5.54         11.65              69.99             1
#                                                                                      1           
#          16.29         1520        45.00       1.30        0.00         8.00               54.30             1
#                                                                                      6           
#          12.70         1462        36.50       1.30        0.00         0.00               37.80             2
#                                                                                                  
#          8.70          1210        26.00       1.30        0.00         5.46               32.76             1
#...                                                                                               
#                                                                                              ...           ...
#            6            30         4                5           3                    4           
#          9.5           1989        31.0        1.3         5.54         3.0                40.84             1
#                                                                 2                    4           
#          19.8          2368        52.0        0.8         5.54         0.0                58.34             1
#                                                                                                  
#          17.48         2822        52.0        0.8         5.54         5.0                63.34             1
#                                                                                      6           
#          12.76         1083        34.5        1.3         0.0          8.95               44.75             1
#                                                                                      0           
#          17.54         1711        48.0        1.3         5.54         0.0                54.84             2


deleted_header=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv",header=None)
deleted_header=deleted_header.add_prefix("col")
print(deleted_header)


#              col0          col1        col2              col3  ...         col11       col12         col13         col14
#0      pickup_year  pickup_month  pickup_day  pickup_dayofweek  ...  tolls_amount  tip_amount  total_amount  payment_type
#1             2016             1           1                 5  ...          5.54       11.65         69.99             
#1
#2             2016             1           1                 5  ...          0.00        8.00         54.30             
#1
#3             2016             1           1                 5  ...          0.00        0.00         37.80             
#2
#4             2016             1           1                 5  ...          0.00        5.46         32.76             
#1
#...            ...           ...         ...               ...  ...           ...         ...           ...           ...
#89556         2016             6          30                 4  ...          5.54         3.0         40.84             
#1
#89557         2016             6          30                 4  ...          5.54         0.0         58.34             
#1
#89558         2016             6          30                 4  ...          5.54         5.0         63.34             
#1
#89559         2016             6          30                 4  ...           0.0        8.95         44.75             
#1
#89560         2016             6          30                 4  ...          5.54         0.0         54.84             
#2
#
#[89561 rows x 15 columns]

data_type=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv",dtype={'pickup_year':float})
print(data_type)

#       pickup_year  pickup_month  pickup_day  pickup_dayofweek  ...  tolls_amount  tip_amount  total_amount  payment_type
#0           2016.0             1           1                 5  ...          5.54       11.65         69.99             
#1
#1           2016.0             1           1                 5  ...          0.00        8.00         54.30             
#1
#2           2016.0             1           1                 5  ...          0.00        0.00         37.80             
#2
#3           2016.0             1           1                 5  ...          0.00        5.46         32.76             
#1
#4           2016.0             1           1                 5  ...          0.00        0.00         18.80             
#2
#...            ...           ...         ...               ...  ...           ...         ...           ...           ...
#89555       2016.0             6          30                 4  ...          5.54        3.00         40.84             
#1
#89556       2016.0             6          30                 4  ...          5.54        0.00         58.34             
#1
#89557       2016.0             6          30                 4  ...          5.54        5.00         63.34             
#1
#89558       2016.0             6          30                 4  ...          0.00        8.95         44.75             
#1
#89559       2016.0             6          30                 4  ...          5.54        0.00         54.84             
#2
#
#[89560 rows x 15 columns]