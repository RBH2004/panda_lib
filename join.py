import pandas as pd

arr1=pd.DataFrame({'A':[1,2,3,4],"B":[11,12,13,14]})
arr2=pd.DataFrame({"C":[21,22,23,24],"D":[31,32,33,34]})

data=arr1.join(arr2)
print(data)

#   A   B   C   D
#0  1  11  21  31
#1  2  12  22  32
#2  3  13  23  33
#3  4  14  24  34


arr1=pd.DataFrame({'A':[1,2,3,4],"B":[11,12,13,14]})
arr2=pd.DataFrame({"C":[21,22],"D":[31,32]})

data=arr1.join(arr2)
print(data)

#   A   B     C     D
#0  1  11  21.0  31.0
#1  2  12  22.0  32.0
#2  3  13   NaN   NaN
#3  4  14   NaN   NaN


arr1=pd.DataFrame({'A':[1,2,3,4],"B":[11,12,13,14]},index=['a','b','c','d'])
arr2=pd.DataFrame({"C":[21,22,23,24],"D":[31,32,33,34]})

data=arr1.join(arr2)
print(data)

#   A   B   C   D
#a  1  11 NaN NaN
#b  2  12 NaN NaN
#c  3  13 NaN NaN
#d  4  14 NaN NaN


arr1=pd.DataFrame({'A':[1,2,3,4],"B":[11,12,13,14]},index=['a','b','c','d'])
arr2=pd.DataFrame({"C":[21,22,23,24],"D":[31,32,33,34]},index=['a','b','c','d'])

data=arr1.join(arr2)
print(data)

#   A   B   C   D
#a  1  11  21  31
#b  2  12  22  32
#c  3  13  23  33
#d  4  14  24  34

