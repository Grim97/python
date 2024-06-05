import pandas as pd
import numpy as np
from numpy.random import randn


def about_series():
    arr = np.array([10,20,30,40])
    ind = ('e','h','g','x')
    # if index length is not eq to data length ValueError will be thrown
    print(pd.Series(data=arr, index=ind))
    # first param is data and 2nd is index. If not given, automatically taken in this order

    dict = {'one': 1, 'two': 2, 'three': 3, 'four':4}
    print("Dict in Series\n", pd.Series(dict))
    # passing a index when using dict will mess up output.
    '''
    print("Dict in Series\n", pd.Series(dict, ind))
    Dict in Series
    e   NaN
    h   NaN
    g   NaN
    x   NaN
    dtype: float64
    '''
    ser = pd.Series([5,4,3,2],ind)
    print(ser['g']) # prints 3
    # if index is string mention str. If int mention int in the braces.

    ser1 = pd.Series([1,2,3],['one','two','three'])
    ser2 = pd.Series([1,2,3],['one','four','five'])
    print(ser1+ser2)
    '''
    for available index, it adds [Note that result is in float] 
    and remaining Nan will be there.
    
    five     NaN
    four     NaN
    one      2.0
    three    NaN
    two      NaN
    dtype: float64
    '''


df = pd.DataFrame(data=randn(2,3),index=['a','b'],columns=['x','y','z'])
print(df)
'''
(data=randn(2,3),index=['a','b','c'],columns=['x','y','z'])
would've raised 
ValueError: Shape of passed values is (2, 3), indices imply (3, 3)
'''
# fetching multiple colomns. Single colomn df['x'] is enough
print(df[['y','z']])

'''
df.drop('z')-> by def axis=0 i.e axis 0 means index. To say colomn,
need to mention axis = 1. 
KeyError: "['z'] not found in axis

And drop doesn't happens inplace.
print(df) will still have three colomns.
For inplace deletion, mention inplace=True
'''
df.drop('z', axis=1, inplace=True)
print(df)

print(df.shape)
'''
(2, 2). df.shape not a callable func.
1st two is row and 2nd is colomn
Thats why axis-0 denotes row and 1 is colomn.
'''

# Fetching row in df. Two ways are there. 1.With name
print(df.loc['b'])
'''
x    1.526270
y   -2.309303
Name: b, dtype: float64
'''
print("iloc\n", df.iloc[0])
'''
iloc
 x   -0.512294
y   -0.265988
Name: a, dtype: float64
'''