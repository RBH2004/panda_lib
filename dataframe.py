import pandas as pd

l=[1,2,3,4,5,6]

var=pd.DataFrame(l)
print(var)

#   0
#0  1
#1  2
#2  3
#3  4
#4  5
#5  6

print(type(var))

#<class 'pandas.core.frame.DataFrame'>


dic={'a':[1,2,3,4],'s':[5,6,7,8]}
var2=pd.DataFrame(dic)
print(var2)

#   a  s
#0  1  5
#1  2  6
#2  3  7
#3  4  8

var3=pd.DataFrame(dic,columns=['a'])
print(var3)
#only those colums we need for the data
#   a
#0  1
#1  2
#2  3
#3  4

list1=[[1,2,3,4],[5,6,7,8]]
x=pd.DataFrame(list1)
print(x)

#   0  1  2  3
#0  1  2  3  4
#1  5  6  7  8

dic1={'s':pd.Series([1,2,3,4]),'d':pd.Series([4,5,6,7])}
print(pd.DataFrame(dic1))

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


skip_row=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv",skiprows=0)
print(skip_row)

#       pickup_year  pickup_month  pickup_day  ...  tip_amount  total_amount  payment_type
#0             2016             1           1  ...       11.65         69.99             1
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