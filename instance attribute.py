# instance attribute
"""
Created on Wed Nov 23 11:27:31 2022

@author: ADMIN
"""
class user:
    course='python'

o=user()
print(user.__dict__)
print(user.course)
print(o.__dict__)
print(o.course)
o.course='java'
print(o.__dict__)
print(o.course)
o2=user()
print(o2.course)