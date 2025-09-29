import pandas as pd


arr1=pd.Series([1,2,3,4])
arr2=pd.Series([11,21,31,41])

data=pd.concat([arr1,arr2])
print(data)

#0     1
#1     2
#2     3
#3     4
#0    11
#1    21
#2    31
#3    41
#dtype: int64


arr1=pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})
arr2=pd.DataFrame({'A':[1,2,3,5],'B':[21,22,23,24]})

data=pd.concat([arr1,arr2])
print(data)

#   A   B
#0  1  11
#1  2  12
#2  3  13
#3  4  14
#0  1  21
#1  2  22
#2  3  23
#3  5  24
