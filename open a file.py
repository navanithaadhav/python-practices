# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 09:37:14 2022

@author: ADMIN
"""
try:
   file=open('Navat.txt','r')
   print(file.read())
except FileNotFoundError:
    print('Error:File Not Found')
else:
    file.close()