# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:12:19 2022

@author: ADMIN
"""
try:
   file=open('Nava.txt','r')
   for line in file:
       print(line)
except FileNotFoundError:
    print('Error:File Not Found')
else:
    file.close()