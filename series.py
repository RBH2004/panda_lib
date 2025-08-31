import pandas as pd

arr1=pd.Series([1,2,3,4])
print(arr1)
#0    1
#1    2
#2    3
#3    4
#dtype: int64

arr2=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(arr2)
#a    1
#b    2
#c    3
#d    4
#dtype: int64


arr3=pd.Series([1,2,3,4],index=['a','b','c','d'],name='First one')
print(arr3)

#a    1
#b    2
#c    3
#d    4
#Name: First one, dtype: int64


dic={'name':['rafid','efaz','fahim','nafiz'],'serial':[1,2,3,4],'rank':[1,2,3,54]}
arr=pd.Series(dic)
print(arr)

#name      [rafid, efaz, fahim, nafiz]
#serial                   [1, 2, 3, 4]
#rank                    [1, 2, 3, 54]
#dtype: object

s=pd.Series(12)
print(s)

#0    12
#dtype: int64

s=pd.Series(12,index=[1,2,3,4,5])
print(s)

#1    12
#2    12
#3    12
#4    12
#5    12
#dtype: int64

s1=pd.Series(12,index=[1,2,3,4,5,6])
s2=pd.Series(12,index=[1,2,3])
print(s1+s2)

#1    24.0
#2    24.0
#3    24.0
#4     NaN
#5     NaN
#6     NaN
#dtype: float64
