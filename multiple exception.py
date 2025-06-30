#handling multible exception error
"""
Created on Tue Nov 22 13:28:22 2022

@author: ADMIN
"""
try:
    a=10/20
    print(a)
    b=[10,20,30,50]
    print(b[10])
except ZeroDivisionError:
    print('denominator cant be zero')
except IndexError:
    print('invalid index')