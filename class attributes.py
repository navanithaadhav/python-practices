# class attributes
"""
Created on Wed Nov 23 11:05:06 2022

@author: ADMIN
"""
class student():
    name='Dev'
    age=25
#getattr method
print(getattr(student,'name'))
print(getattr(student,'age'))
print(getattr(student,'gender','no such attribute found'))
# dot notation
print(student.name)
print(student.age)
#setattr
setattr(student,'name','nava')
print(student.name)
setattr(student,'gender','female')
print(student.gender)
student.city='theni'
print(student.city)
print(student.__dict__)
delattr(student,'age')
print(student.__dict__)
del student.gender
print(student.__dict__)