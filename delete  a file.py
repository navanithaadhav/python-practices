# delect a file in pi
"""
Created on Mon Nov 28 10:45:22 2022

@author: ADMIN
"""
import os
if os.path.exists('test.txt'):
    os.remove('test.txt')
    print('file delete')
else:
    print('file not found')