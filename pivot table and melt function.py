import pandas as pd

var = pd.DataFrame({
    "days": [1, 2, 3, 4, 5, 6],
    "eng": [10, 12, 14, 15, 16, 12],
    "maths": [17, 18, 19, 13, 14, 16]
})

print(pd.melt(var))


#   variable  value
#0      days      1
#1      days      2
#2      days      3
#3      days      4
#4      days      5
#5      days      6
#6       eng     10
#7       eng     12
#8       eng     14
#9       eng     15
#10      eng     16
#11      eng     12
#12    maths     17
#13    maths     18
#14    maths     19
#15    maths     13
#16    maths     14
#17    maths     16

print(pd.melt(var,id_vars=['days']))
#    days variable  value
#0      1      eng     10
#1      2      eng     12
#2      3      eng     14
#3      4      eng     15
#4      5      eng     16
#5      6      eng     12
#6      1    maths     17
#7      2    maths     18
#8      3    maths     19
#9      4    maths     13
#10     5    maths     14
#11     6    maths     16

print(pd.melt(var,id_vars=['days'],var_name='Cse'))

#    days    Cse  value
#0      1    eng     10
#1      2    eng     12
#2      3    eng     14
#3      4    eng     15
#4      5    eng     16
#5      6    eng     12
#6      1  maths     17
#7      2  maths     18
#8      3  maths     19
#9      4  maths     13
#10     5  maths     14
#11     6  maths     16

print(pd.melt(var,id_vars=['days'],var_name='Cse',value_name='Rafid'))
#
#    days    Cse  Rafid
#0      1    eng     10
#1      2    eng     12
#2      3    eng     14
#3      4    eng     15
#4      5    eng     16
#5      6    eng     12
#6      1  maths     17
#7      2  maths     18
#8      3  maths     19
#9      4  maths     13
#10     5  maths     14
#11     6  maths     16


var = pd.DataFrame({
    "days": [1, 2, 3, 4, 5, 6],
    "st_name": ["a", "b", "c", "a", "b", "c"],
    "eng": [10, 12, 14, 15, 16, 12],
    "maths": [17, 18, 19, 13, 14, 16]
})
print(var.pivot(index='days',columns='st_name'))

#          eng             maths
#st_name     a     b     c     a     b     c
#days
#1        10.0   NaN   NaN  17.0   NaN   NaN
#2         NaN  12.0   NaN   NaN  18.0   NaN
#3         NaN   NaN  14.0   NaN   NaN  19.0
#4        15.0   NaN   NaN  13.0   NaN   NaN
#5         NaN  16.0   NaN   NaN  14.0   NaN
#6         NaN   NaN  12.0   NaN   NaN  16.0


print(var.pivot(index='days',columns='st_name',values='eng'))

#st_name     a     b     c
#days
#1        10.0   NaN   NaN
#2         NaN  12.0   NaN
#3         NaN   NaN  14.0
#4        15.0   NaN   NaN
#5         NaN  16.0   NaN
#6         NaN   NaN  12.0

var = pd.DataFrame({
    "days": [1, 2, 3, 4, 5, 6],
    "st_name": ["a", "b", "c", "a", "b", "c"],
    "eng": [10, 12, 14, 15, 16, 12],
    "maths": [17, 18, 19, 13, 14, 16]
})

print(var.pivot_table(index='st_name',columns='days',aggfunc='mean'))

#          eng                               maths
#days        1     2     3     4     5     6     1     2     3     4     5     6
#st_name
#a        10.0   NaN   NaN  15.0   NaN   NaN  17.0   NaN   NaN  13.0   NaN   NaN
#b         NaN  12.0   NaN   NaN  16.0   NaN   NaN  18.0   NaN   NaN  14.0   NaN
#c         NaN   NaN  14.0   NaN   NaN  12.0   NaN   NaN  19.0   NaN   NaN  16.0
print(var.pivot_table(index='st_name',columns='days',aggfunc='mean',margins=True))
#          eng                                          maths
#days        1     2     3     4     5     6        All     1     2     3     4     5     6        All   
#st_name
#a        10.0   NaN   NaN  15.0   NaN   NaN  12.500000  17.0   NaN   NaN  13.0   NaN   NaN  15.000000   
#b         NaN  12.0   NaN   NaN  16.0   NaN  14.000000   NaN  18.0   NaN   NaN  14.0   NaN  16.000000   
#c         NaN   NaN  14.0   NaN   NaN  12.0  13.000000   NaN   NaN  19.0   NaN   NaN  16.0  17.500000   
#All      10.0  12.0  14.0  15.0  16.0  12.0  13.166667  17.0  18.0  19.0  13.0  14.0  16.0  16.166667   