# class method
"""
Created on Wed Nov 23 11:43:59 2022

@author: ADMIN
"""
class student:
    name='nava'
    age=27
    def printall():
       print('name:',student.name)
       print('age:',student.age)
student.printall()
print(student.__dict__)
print(getattr(student,'printall'))
getattr(student,'printall')
student.__dict__['printall']()
