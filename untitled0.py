# propertiy decorator
"""
Created on Wed Nov 23 14:20:56 2022

@author: ADMIN
"""
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def msg(self):
        return self.name  + 'is' + str(self.age) + 'years old'
o=user('nava',25)
print(o.name)
print(o.age)
print(o.msg())
o.age=45
print(o.age)
print(o.msg())
print('-------------------------------------------------')
#priperty decorator
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @property
    def msg(self):
        return self.name  + 'is' + str(self.age) + 'years old'
o=user('nava',25)
print(o.name)
print(o.age)
print(o.msg)
o.age=45
print(o.age)
print(o.msg)
