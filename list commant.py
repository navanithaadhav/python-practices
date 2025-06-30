# list comant
"""
Created on Wed Nov  2 17:07:51 2022

@author: ADMIN
"""
a=[1,2,3,4,5]
print(a)
print(type(a))
a[0]=100
print(a)
print(a[1])
print(a[0:3])
print(a[2:])
print(a[:3])
print(".........")
a=[1,True,"ram",2.5,[1,2,3,4]]
print(a[0],"type is",type(a[0]))
print(a[1],"type is",type(a[1]))
print(a[2],"type is",type(a[2]))
print(a[3],"type is",type(a[3]))
print(a[4],"type is",type(a[4]))
print(a[4][1],"type is",type(a[4][1]))
print(a[4][2])
print("...........")
a=[1,2,3,4,5]
print(a)
a.clear()
print(a)
a=[1,2,3,4,5]
b=a.copy()
print(b)
print(a.count(2))
print(a.index(3))
print(len(a))
print(min(a))
print(max(a))
print(a)
a.pop(0)
print(a)
a=[1,2,3,4,5]
a.remove(3)
print(a)
a.reverse()
print(a)
print("...........")
names=["nava"]
print(names)
names.append("ram")
names.append("sam")
names.append("gam")
print(names)
name2=["ravi","dev"]
names.extend(name2)
print(names)
names.insert(0,"surya")
print(names)
print(list(range(5)))
print(list("nava"))
a=[10,7,96,25,100,4]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["orange","apple","zebra"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.sort(key=len)
print(a)










