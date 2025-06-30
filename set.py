# Set in python
"""
Created on Thu Nov  3 16:09:39 2022

@author: ADMIN
"""
'''names={"ram","sam","ravi"}
print(names)
print(type(names))
for name in names:
    print(name)
names.add("sara")
print(names)
a={"sis","dev","raj"}
names.update(a)
print(names)
names.remove('sara')
print(names)
names.discard('sam')
print(names)
names.pop()
print(names)
names.clear ()
print(names)
print("......................")

a={'nava','nava','ram','raj'}
print(a)
a={1,2,3,4}
b={'a','b','c','d'}
c=a.union(b)
print(c)
a.update(b)
print(a)
'''
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)
c=a.isdisjoint(a)
print(c)
c=a.issubset(b)
print(c)
a={5,6,7}
b={5,6,7}
c=a.issuperset(b)
print(c)