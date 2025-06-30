# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 12:10:41 2022

@author: ADMIN
"""

para=[]
print("Enter a para:")
while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
print(para)
output='\n'.join(para)
print(output) 