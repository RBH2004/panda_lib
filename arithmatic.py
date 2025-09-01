import pandas as pd

arr=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})

arr["C"]=arr["A"]+arr["B"]

print(arr)
#   A  B   C
#0  1  5   6
#1  2  6   8
#2  3  7  10
#3  4  8  12