# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:14:03 2022

@author: ADMIN
"""

try:
   file=open('Nava.txt','w')
   file.write('This is Nava from Theni')
   file.close()
   file=open('Nava.txt','r')
   for line in file:
       print(line)
except FileNotFoundError:
    print('Error:File Not Found')
else:
    file.close()