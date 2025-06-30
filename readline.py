# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:03:36 2022

@author: ADMIN
"""

try:
   file=open('Nava.txt','r')
   #print(file.readlines())
   print(file.readline())
   print(file.readline(5))
except FileNotFoundError:
    print('Error:File Not Found')
else:
    file.close()