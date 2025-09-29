import pandas as pd

data=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv")
print(data)

data1=data.replace(to_replace=2016,value=2017)
print(data1)

#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0             2017             1           1  ...       11.65         69.99             1
#1             2017             1           1  ...        8.00         54.30             1
#2             2017             1           1  ...        0.00         37.80             2
#3             2017             1           1  ...        5.46         32.76             1
#4             2017             1           1  ...        0.00         18.80             2
#...            ...           ...         ...  ...         ...           ...           ...
#89555         2017             6          30  ...        3.00         40.84             1
#89556         2017             6          30  ...        0.00         58.34             1
#89557         2017             6          30  ...        5.00         63.34             1
#89558         2017             6          30  ...        8.95         44.75             1
#89559         2017             6          30  ...        0.00         54.84             2
#
#[89560 rows x 15 columns]

data2=data.replace([11.65,8.00],2017)
print(data2)

#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0             2016             1           1  ...     2017.00         69.99             1
#1             2016             1           1  ...     2017.00         54.30             1
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

data.loc[0,'pickup_year']="Rafid"
data.loc[1,'pickup_year']="efaz"
data.loc[2,'pickup_year']="nafiz"
data.loc[3,'pickup_year']="Fahim"
data.loc[4,'pickup_year']="Tofa"

print(data)
#      pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0           Rafid             1           1  ...       11.65         69.99             1
#1            efaz             1           1  ...        8.00         54.30             1
#2           nafiz             1           1  ...        0.00         37.80             2
#3           Fahim             1           1  ...        5.46         32.76             1
#4            Tofa             1           1  ...        0.00         18.80             2
#...           ...           ...         ...  ...         ...           ...           ...
#89555        2016             6          30  ...        3.00         40.84             1
#89556        2016             6          30  ...        0.00         58.34             1
#89557        2016             6          30  ...        5.00         63.34             1
#89558        2016             6          30  ...        8.95         44.75             1
#89559        2016             6          30  ...        0.00         54.84             2
#[89560 rows x 15 columns]


data3=data.replace('[A-Za-z]','cse',regex=True)
print(data3)
#           pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0      csecsecsecsecse             1           1  ...       11.65         69.99             1     
#1         csecsecsecse             1           1  ...        8.00         54.30             1     
#2      csecsecsecsecse             1           1  ...        0.00         37.80             2     
#3      csecsecsecsecse             1           1  ...        5.46         32.76             1     
#4         csecsecsecse             1           1  ...        0.00         18.80             2     
#...                ...           ...         ...  ...         ...           ...           ...     
#89555             2016             6          30  ...        3.00         40.84             1     
#89556             2016             6          30  ...        0.00         58.34             1     
#89557             2016             6          30  ...        5.00         63.34             1     
#89558             2016             6          30  ...        8.95         44.75             1     
#89559             2016             6          30  ...        0.00         54.84             2     
#
#[89560 rows x 15 columns]

data4=data.replace({'pickup_year':'[A-Z]'},22,regex=True)
print(data4)

#      pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0              22             1           1  ...       11.65         69.99             1
#1            efaz             1           1  ...        8.00         54.30             1
#2           nafiz             1           1  ...        0.00         37.80             2
#3              22             1           1  ...        5.46         32.76             1
#4              22             1           1  ...        0.00         18.80             2
#...           ...           ...         ...  ...         ...           ...           ...
#89555        2016             6          30  ...        3.00         40.84             1
#89556        2016             6          30  ...        0.00         58.34             1
#89557        2016             6          30  ...        5.00         63.34             1
#89558        2016             6          30  ...        8.95         44.75             1
#89559        2016             6          30  ...        0.00         54.84             2
#
#[89560 rows x 15 columns]

data5=data.replace(8.00,method='ffill',limit=2)
print(data5)
#
#      pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0           Rafid             1           1  ...       11.65         69.99             1
#1            efaz             1           1  ...       11.65         54.30             1
#2           nafiz             1           1  ...        0.00         37.80             2
#3           Fahim             1           1  ...        5.46         32.76             1
#4            Tofa             1           1  ...        0.00         18.80             2
#...           ...           ...         ...  ...         ...           ...           ...
#89555        2016             6          30  ...        3.00         40.84             1
#89556        2016             6          30  ...        0.00         58.34             1
#89557        2016             6          30  ...        5.00         63.34             1
#89558        2016             6          30  ...        8.95         44.75             1
#89559        2016             6          30  ...        0.00         54.84             2
#
#[89560 rows x 15 columns]


data.replace(8.00,method='ffill',limit=2,inplace=True)
print(data)

#      pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0           Rafid             1           1  ...       11.65         69.99             1
#1            efaz             1           1  ...       11.65         54.30             1
#2           nafiz             1           1  ...        0.00         37.80             2
#3           Fahim             1           1  ...        5.46         32.76             1
#4            Tofa             1           1  ...        0.00         18.80             2
#...           ...           ...         ...  ...         ...           ...           ...
#89555        2016             6          30  ...        3.00         40.84             1
#89556        2016             6          30  ...        0.00         58.34             1
#89557        2016             6          30  ...        5.00         63.34             1
#89558        2016             6          30  ...        8.95         44.75             1
#89559        2016             6          30  ...        0.00         54.84             2
#
#[89560 rows x 15 columns]