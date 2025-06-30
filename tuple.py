# Tuple in python
"""
Created on Thu Nov  3 11:17:34 2022

@author: ADMIN
"""
a=(1,2.5,True,"ram")
print(a)
print(type(a))
print(a[0])
print(a[1])
print(a[0:2])
print(a[-1])
print(a[::-1])
b=list(a)
print(b)
b.append('raja')
print(b)
a=tuple(b)
print(type(a))
for i in a:
    print(i)
if 'raja' in a:
    print('raja is found')
else:
    print('not found')
a=(1)
print(type(a))
a=(1,)
print(type(a))
a=(1,2,3,4)
b=(5,6,7,8)
c=a+b
print(c)
print(c.count(2))
c=(a,b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])
x=("nava",)*5
print(x)
a=(1,2,3,4)
print(max(a))
print(min(a))
print(a)
del a