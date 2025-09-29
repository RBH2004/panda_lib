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


data=pd.concat([arr1,arr2],axis=1)
print(data)

#   A   B  A   B
#0  1  11  1  21
#1  2  12  2  22
#2  3  13  3  23
#3  4  14  5  24



arr1=pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})
arr2=pd.DataFrame({'A':[1,2],'B':[21,22]})

data=pd.concat([arr1,arr2],axis=1)
print(data)

#   A   B    A     B
#0  1  11  1.0  21.0
#1  2  12  2.0  22.0
#2  3  13  NaN   NaN
#3  4  14  NaN   NaN

data=pd.concat([arr1,arr2],axis=1,join="outer")
print(data)
#   A   B    A     B
#0  1  11  1.0  21.0
#1  2  12  2.0  22.0
#2  3  13  NaN   NaN
#3  4  14  NaN   NaN

data=pd.concat([arr1,arr2],axis=1,join='inner')
print(data)

#   A   B  A   B
#0  1  11  1  21
#1  2  12  2  22

arr1=pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})
arr2=pd.DataFrame({'A':[1,2,3,5],'B':[21,22,23,24]})

data=pd.concat([arr1,arr2],keys=['d1','d2'])
print(data)
#      A   B
#d1 0  1  11
#   1  2  12
#   2  3  13
#   3  4  14
#d2 0  1  21
#   1  2  22
#   2  3  23
#   3  5  24


data=pd.concat([arr1,arr2],keys=['d1','d2'],axis=1)
print(data)

#  d1     d2    
#   A   B  A   B
#0  1  11  1  21
#1  2  12  2  22
#2  3  13  3  23
#3  4  14  5  24
