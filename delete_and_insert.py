import pandas as pd

arr=pd.DataFrame({"A":[1,2,3,4],'B':[4,5,6,7]})

arr.insert(1,'python',arr["A"])
print(arr)

#   A  python  B
#0  1       1  4
#1  2       2  5
#2  3       3  6
#3  4       4  7

arr["python_2"]=arr["B"][:3:]
print(arr)

#   A  python  B  python_2
#0  1       1  4       4.0
#1  2       2  5       5.0
#2  3       3  6       6.0
#3  4       4  7       NaN

arr.pop("A")
print(arr)

#   python  B  python_2
#0       1  4       4.0
#1       2  5       5.0
#2       3  6       6.0
#3       4  7       NaN

del arr["B"]
print(arr)

#   python  python_2
#0       1       4.0
#1       2       5.0
#2       3       6.0
#3       4       NaN