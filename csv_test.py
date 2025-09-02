import pandas as pd

d={'a':[1,2,3,4,5,6,7],"b":[1,2,3,4,5,6,7]}
arr=pd.DataFrame(d)
print(arr)

arr.to_csv("testing.csv")
print(arr)
arr.to_csv("testing.csv",index=False,header=[1,2])
print(arr)
