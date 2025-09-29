import pandas as pd

arr1=pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})
arr2=pd.DataFrame({'A':[1,2,3,5],'C':[21,22,23,24]})

data=pd.merge(arr1,arr2,on="A")
print(data)

#   A   B   C
#0  1  11  21
#1  2  12  22
#2  3  13  23

data2=pd.merge(arr1,arr2,how='inner')
print(data2)

#   A   B   C
#0  1  11  21
#1  2  12  22
#2  3  13  23

data2=pd.merge(arr1,arr2,how='left')
print(data2)

#   A   B     C
#0  1  11  21.0
#1  2  12  22.0
#2  3  13  23.0
#3  4  14   NaN

data3=pd.merge(arr1,arr2,how='right')
print(data3)

#   A     B   C
#0  1  11.0  21
#1  2  12.0  22
#2  3  13.0  23
#3  5   NaN  24

data4=pd.merge(arr1,arr2,how='outer')
print(data4)

#   A     B     C
#0  1  11.0  21.0
#1  2  12.0  22.0
#2  3  13.0  23.0
#3  4  14.0   NaN
#4  5   NaN  24.0

data5=pd.merge(arr1,arr2,how='outer',indicator=True)
print(data5)

#   A     B     C      _merge
#0  1  11.0  21.0        both
#1  2  12.0  22.0        both
#2  3  13.0  23.0        both
#3  4  14.0   NaN   left_only
#4  5   NaN  24.0  right_only

arr1=pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})
arr2=pd.DataFrame({'A':[1,2,3,5],'B':[21,22,23,24]})

data=pd.merge(arr1,arr2,left_index=True,right_index=True)
print(data)

#   A_x  B_x  A_y  B_y
#0    1   11    1   21
#1    2   12    2   22
#2    3   13    3   23
#3    4   14    5   24
#

data=pd.merge(arr1,arr2,left_index=True,right_index=True,suffixes=['_name','_id'])
print(data)
#   A_name  B_name  A_id  B_id
#0       1      11     1    21
#1       2      12     2    22
#2       3      13     3    23
#3       4      14     5    24

