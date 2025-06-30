#try block in pi
"""
Created on Tue Nov 22 11:29:04 2022

@author: ADMIN

a=10/0
print(a)
"""
try:
    a=10/0
except Exception as e:
    print(e)
#try else block in pi
try:
    a=10/15
except Exception as e:
    print(e)
else:
    print('A value:',a)
#finally block in pi
try:
    a=10/15
except Exception as e:
    print(e)
else:
    print('A value:',a)    
finally:
    print('Thank you')
print('---------------------------------------')
try:
    a=10/0
except Exception as e:
    print(e)
else:
    print('A value:',a)    
finally:
    print('Thank you')
