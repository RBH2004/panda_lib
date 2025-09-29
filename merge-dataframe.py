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



