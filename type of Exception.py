#type of Exception
"""
Created on Tue Nov 22 11:45:48 2022

@author: ADMIN
"""
'''print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))'''

# name error exception
try:
    print(a)
except NameError as e:
    print('A is not defined')
#zerodivition error exception
try:
    print(10/0)
except ZeroDivisionError as e:
    print('denominator cant be zero')
#value error exception
try:
    a=int('nava')
except ValueError as e:
    print('please enter numbers only')
#index error exception
try:
    a=[10,20,30,40]
    print(a[10])
except IndexError as e:
    print('invalid index')
try:
    a=[10,20,30,40]
    print(a[0])
except IndexError as e:
    print('invalid index')
#file not found exception
try:
    f=open('test.txt')
except FileNotFoundError :
    print('file not found')
else:
    print(f.read())