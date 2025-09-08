import pandas as pd

l=[1,2,3,4,5,6]

var=pd.DataFrame(l)
print(var)

#   0
#0  1
#1  2
#2  3
#3  4
#4  5
#5  6

print(type(var))

#<class 'pandas.core.frame.DataFrame'>


dic={'a':[1,2,3,4],'s':[5,6,7,8]}
var2=pd.DataFrame(dic)
print(var2)

#   a  s
#0  1  5
#1  2  6
#2  3  7
#3  4  8

var3=pd.DataFrame(dic,columns=['a'])
print(var3)
#only those colums we need for the data
#   a
#0  1
#1  2
#2  3
#3  4

list1=[[1,2,3,4],[5,6,7,8]]
x=pd.DataFrame(list1)
print(x)

#   0  1  2  3
#0  1  2  3  4
#1  5  6  7  8

dic1={'s':pd.Series([1,2,3,4]),'d':pd.Series([4,5,6,7])}
print(pd.DataFrame(dic1))


#   s  d
#0  1  4
#1  2  5
#2  3  6
#3  4  7

