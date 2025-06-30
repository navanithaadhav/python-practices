# init method
"""
Created on Wed Nov 23 12:06:39 2022

@author: ADMIN
"""
class user:
    def __init__ (self,name):
       print('call when new instance created')
       self.name=name
    def printall(self):
        print('name:',self.name)
o=user('nava')
o.printall()
print(o.__dict__)
o1=user('dev')
o1.printall()
print(o1.__dict__)
print(user.__dict__)

