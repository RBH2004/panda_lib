import pandas as pd

d = {'a':[1,2,3,4,5,6,7],"b":[1,2,3,4,5,6,7]}
arr=pd.DataFrame(d)
print(arr)


#   a  b
#0  1  1
#1  2  2
#2  3  3
#3  4  4
#4  5  5
#5  6  6
#6  7  7

arr.to_csv("testing.csv")
print(arr)

#   a  b
#0  1  1
#1  2  2
#2  3  3
#3  4  4
#4  5  5
#5  6  6
#6  7  7

arr.to_csv("testing.csv",index=False,header=[1,2])
print(arr)

#1,2
#1,1
#2,2
#3,3
#4,4
#5,5
#6,6
#7,7
