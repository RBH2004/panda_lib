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
