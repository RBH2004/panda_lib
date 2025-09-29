import pandas as pd

arr1=pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})
arr2=pd.DataFrame({'A':[1,2,3,5],'C':[21,22,23,24]})

data=pd.merge(arr1,arr2,on="A")
print(data)

#   A   B   C
#0  1  11  21
#1  2  12  22
#2  3  13  23
