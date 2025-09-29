import pandas as pd


data=pd.DataFrame({'name':['a','b','c','d','a','b','a','b','a','c','c','d'],
                   's-1':[12,13,14,12,13,14,15,23,25,16,10,34],
                   's_2':[23,24,25,26,28,28,29,30,25,34,35,56]})


new_data=data.groupby('name')


for i,j in new_data:
    print(i)
    print(j)
    print()

#a
#  name  s-1  s_2
#0    a   12   23
#4    a   13   28
#6    a   15   29
#8    a   25   25
#
#b
#  name  s-1  s_2
#1    b   13   24
#5    b   14   28
#7    b   23   30
#
#c
#   name  s-1  s_2
#2     c   14   25
#9     c   16   34
#10    c   10   35
#
#d
#   name  s-1  s_2
#3     d   12   26
#11    d   34   56

x=new_data.get_group('a')
print(x)

#  name  s-1  s_2
#0    a   12   23
#4    a   13   28
#6    a   15   29
#8    a   25   25

print(new_data.min()) #similarly max(), mean() can be used
#name
#a      12   23
#b      13   24
#c      10   25
#d      12   26

a_list=list(new_data)
print(a_list)

#[('a',   name  s-1  s_2
#0    a   12   23
#4    a   13   28
#6    a   15   29
#8    a   25   25), ('b',   name  s-1  s_2
#1    b   13   24
#5    b   14   28
#7    b   23   30), ('c',    name  s-1  s_2
#2     c   14   25
#9     c   16   34
#10    c   10   35), ('d',    name  s-1  s_2
#3     d   12   26
#11    d   34   56)]