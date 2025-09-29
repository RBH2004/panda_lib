import pandas as pd


arr1=pd.DataFrame({'A':[1,2,3,4],"B":[11,12,13,14]},index=['a','b','c','d'])
arr2=pd.DataFrame({"C":[21,22],"D":[31,32]},index=['a','b'])

data=arr1.append(arr2)
print(data)
